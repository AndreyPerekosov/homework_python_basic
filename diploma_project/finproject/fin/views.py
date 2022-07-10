import json

from django.shortcuts import render, redirect
import requests
from datetime import timedelta, datetime

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from numpy import unicode

from fin.forms import CalcForm
from fin.models import Portfolio, Stock
from finauth.models import FinUser
from fin.service.service import calc, colors

import pandas as pd

from django.http import Http404, HttpResponse
import json
import django.apps as apps

API = {'tinkoff': 'https://api-invest.tinkoff.ru/openapi/market/candles'}


def index(request):
    user = request.user
    if user.is_anonymous:
        return render(request, 'fin/index.html')
    else:
        model_user = FinUser.objects.get(id=user.pk)
        context = {'user': model_user}
        return render(request, 'fin/index.html', context=context)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class PortfolioDetailView(PageTitleMixin, DetailView):
    model = Portfolio
    page_title = 'Portfolio detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['data'] = json.loads(instance.data)
        context['colors'] = json.loads(instance.colors)
        return context


class PortfolioCreateView(PageTitleMixin, CreateView):
    model = Portfolio
    page_title = 'Portfolio Create'
    success_url = reverse_lazy('fin:index')
    fields = ['name_portfolio']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PortfolioUpdateView(PageTitleMixin, UpdateView):
    model = Portfolio
    page_title = 'Portfolio update'
    success_url = reverse_lazy('fin:index')
    fields = ['name_portfolio']
    template_name = 'fin/portfolio_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        stocks = Stock.objects.exclude(portfolio__stock=obj.id)
        context['stocks'] = stocks
        return context


def delete_portfolio(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    portfolio.delete()
    return render(request, 'fin/index.html')


def add_stock(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    stock_name = request.POST['add_stock']
    stock = Stock.objects.filter(name__startswith=stock_name).first()
    portfolio.stock_set.add(stock)
    return redirect('fin:update_portfolio', portfolio_id)


def remove_stock(request, portfolio_id, stock_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    stock = Stock.objects.get(id=stock_id)
    portfolio.stock_set.remove(stock)
    return redirect('fin:update_portfolio', portfolio_id)


def calc_portfolio(request, portfolio_id):
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            # preparing data
            # grab params from the form
            token = form.cleaned_data['token']
            # calculate period of time
            number_iter = form.cleaned_data['number_iter']
            risk = form.cleaned_data['risk'] / 100
            delta = timedelta(days=form.cleaned_data['months'] * 31)
            time_today = datetime.now()
            time_past = time_today - delta
            # formatting data for api request
            time_today = time_today.strftime("%Y-%m-%dT%H:%M:%S%z+03:00")
            time_past = time_past.strftime("%Y-%m-%dT%H:%M:%S%z+03:00")
            # get list of stock
            portfolio = Portfolio.objects.get(id=portfolio_id)
            stocks = portfolio.stock_set.all()
            # preparing headers
            headers = {'Authorization': 'Bearer ' + token, 'accept': 'application/json'}
            # process request data from api
            df = pd.DataFrame()
            for stock in stocks:
                payload = {'figi': stock.figi, 'from': time_past, 'to': time_today, 'interval': 'month'}
                response = requests.get(API['tinkoff'], headers=headers, params=payload)
                dump_data = response.json()
                dates = [date['time'].split('T')[0] for date in dump_data['payload']['candles']]
                tmp = pd.DataFrame({stock.name: [prices['c'] for prices in dump_data['payload']['candles']]},
                                   index=dates)
                df = pd.concat([df, tmp], axis=1)
            portfolio_data = calc(df, number_iter, risk)
            portfolio.date_update = datetime.now()
            portfolio.data = json.dumps(portfolio_data['data'])
            portfolio.volatility = portfolio_data['vol_ret']['Volatility']
            portfolio.portfolio_return = portfolio_data['vol_ret']['Returns']
            portfolio.sharp = portfolio_data['Sharp']
            colors_list = []
            for color in colors(len(stocks)):
                colors_list.append(color)
            portfolio.colors = json.dumps(colors_list)
            portfolio.save()
            return redirect('fin:detail_portfolio', portfolio_id)
        else:
            return render(request, 'fin/calc_portfolio.html', {'form': form})
    else:
        form = CalcForm()
        return render(request, 'fin/calc_portfolio.html', {'form': form})


