from django.urls import path

import fin.views as fin
from . import views
app_name = 'fin'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_portfolio/', fin.PortfolioCreateView.as_view(), name='create_portfolio'),
    path('update_portfolio/<int:pk>/', fin.PortfolioUpdateView.as_view(), name='update_portfolio'),
    path('detail_portfolio/<int:pk>/', fin.PortfolioDetailView.as_view(), name='detail_portfolio'),
]
