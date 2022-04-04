from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import finauth.views as finauth
from . import views
app_name = 'finauth'
urlpatterns = [
    path('register/', finauth.FinUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
