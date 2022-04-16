from django.views.generic import CreateView

from finauth.form import FinUserCreateForm
from finauth.models import FinUser


class FinUserCreateView(CreateView):
    model = FinUser
    success_url = '/fin'
    form_class = FinUserCreateForm
