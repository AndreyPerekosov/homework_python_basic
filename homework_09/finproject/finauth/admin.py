from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from finauth.models import FinUser


class FinUserAdmin(UserAdmin):
    pass


admin.site.register(FinUser, FinUserAdmin)
