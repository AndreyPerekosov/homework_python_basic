from django.contrib.auth.forms import UserCreationForm

from finauth.models import FinUser


class FinUserCreateForm(UserCreationForm):
    class Meta:
        model = FinUser
        fields = ('username', 'email', 'password1', 'password2')
