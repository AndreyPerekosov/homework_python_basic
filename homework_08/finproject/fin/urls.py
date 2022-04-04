from django.urls import path

from . import views
app_name = 'fin'
urlpatterns = [
    path('', views.index, name='index')
]
