from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from datetime import timedelta, datetime

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from fin.forms import CalcForm
from fin.models import Portfolio, Stock
from finauth.models import FinUser

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
        stocks = Stock.objects.all()
        context['stocks'] = stocks
        return context


def delete_portfolio(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    portfolio.delete()
    return render(request, 'fin/index.html')


def add_stock(request, portfolio_id, stock_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    stock = Stock.objects.get(id=stock_id)
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
            days = form.cleaned_data['days']
            delta = timedelta(days=days)
            time_today = datetime.now()
            time_past = time_today - delta
            # formatting data for api request
            time_today = time_today.strftime("%Y-%m-%dT%H:%M:%S%z+03:00")
            time_past = time_past.strftime("%Y-%m-%dT%H:%M:%S%z+03:00")
            # get list of stock
            portfolio = Portfolio.objects.get(id=portfolio_id)
            stocks = portfolio.stock_set.all()
            dict_data = {}
            # preparing headers
            headers = {'Authorization': 'Bearer ' + token, 'accept': 'application/json'}
            # process request data from api
            for stock in stocks:
                payload = {'figi': stock.figi, 'from': time_past, 'to': time_today, 'interval': 'day'}
                response = requests.get(API['tinkoff'], headers=headers, params=payload)
                dump_data = response.json()
                dict_data[stock.name] = dump_data['payload']['candles']
            print(dict_data)
            return redirect('fin:detail_portfolio', portfolio_id)
    else:
        form = CalcForm()
        return render(request, 'fin/calc_portfolio.html', {'form': form})
