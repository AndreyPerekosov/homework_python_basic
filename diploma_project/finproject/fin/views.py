from django.shortcuts import render


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from fin.models import Portfolio
from finauth.models import FinUser


def index(request):
    user = request.user
    if user.is_anonymous:
        return render(request, 'fin/index.html')
    else:
        model_user = FinUser.objects.get(id = user.pk)
        portfolios = model_user.portfolio_set.all()
        context = {'portfolios': portfolios}
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
    fields = '__all__'


class PortfolioUpdateView(PageTitleMixin, UpdateView):
    model = Portfolio
    page_title = 'Portfolio update'
    success_url = reverse_lazy('fin:index')
    fields = '__all__'
