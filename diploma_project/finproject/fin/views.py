from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from fin.models import Stock


def index(request):
    return render(request, 'fin/index.html')


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class StockDetailView(PageTitleMixin, DetailView):
    model = Stock
    page_title = 'Stock detail'


class StockCreateView(CreateView):
    model = Stock
    success_url = reverse_lazy('fin:index')
    fields = '__all__'


class StockUpdateView(UpdateView):
    model = Stock
    success_url = reverse_lazy('fin:index')
    fields = '__all__'
