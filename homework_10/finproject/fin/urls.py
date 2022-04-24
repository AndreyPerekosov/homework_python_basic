from django.urls import path

import fin.views as fin
from . import views
app_name = 'fin'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_stock/', fin.StockCreateView.as_view(), name='create stock'),
    path('update_stock/<int:pk>/', fin.StockUpdateView.as_view(), name='update stock')
]
