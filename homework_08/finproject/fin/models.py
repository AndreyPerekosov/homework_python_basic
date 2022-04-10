from django.db import models
from finauth.models import FinUser

# class User(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200, unique=True)
#
#     def __str__(self):
#         return f'name: {self.name} email:{self.email}'


class Portfolio(models.Model):
    name_portfolio = models.CharField(max_length=200)
    data = models.JSONField(null=True)
    date_update = models.DateField(auto_now=True)
    user = models.ForeignKey(FinUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'full_name: {self.name_portfolio} data:{self.data}, ' \
               f'date: {self.date_update}'


class Stock(models.Model):
    full_name = models.CharField(max_length=200)
    tick = models.CharField(max_length=50, blank=True)
    price = models.FloatField(null=True)
    date_update = models.DateField(auto_now=True)
    desc = models.TextField(blank=True)
    portfolio = models.ManyToManyField(Portfolio)
    user = models.ManyToManyField(FinUser)

    def __str__(self):
        return f'full_name: {self.full_name} tick:{self.tick}, ' \
               f'date {self.date_update}'
