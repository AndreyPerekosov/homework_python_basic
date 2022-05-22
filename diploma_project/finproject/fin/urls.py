from django.urls import path

import fin.views as fin
from . import views
app_name = 'fin'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_portfolio/', fin.PortfolioCreateView.as_view(), name='create_portfolio'),
    path('update_portfolio/<int:pk>/', fin.PortfolioUpdateView.as_view(), name='update_portfolio'),
    path('detail_portfolio/<int:pk>/', fin.PortfolioDetailView.as_view(), name='detail_portfolio'),
    path('delete_portfolio/<int:pk>/', views.delete_portfolio, name='delete_portfolio'),
    path('portfolio/<int:portfolio_id>add_stock/<int:stock_id>/', views.add_stock, name='add_stock'),
    path('remove_stock/<int:portfolio_id>/<int:stock_id>/', views.remove_stock, name='remove_stock'),
    path('calc_portfolio/<int:portfolio_id>/', views.calc_portfolio, name='calc_portfolio'),
]
