from django.db import models
from finauth.models import FinUser

class Portfolio(models.Model):
    name_portfolio = models.CharField(max_length=200)
    data = models.JSONField(null=True)
    date_update = models.DateField(auto_now=True)
    user = models.ForeignKey(FinUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'full_name: {self.name_portfolio} data:{self.data}, ' \
               f'date: {self.date_update}'


class Stock(models.Model):
    figi= models.CharField(max_length=50, blank=True)
    ticker = models.CharField(max_length=50, blank=True)
    currency = models.CharField(max_length=50, blank=True)
    lot = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    date_update = models.DateField(auto_now=True)
    desc = models.TextField(blank=True)
    portfolio = models.ManyToManyField(Portfolio)
    user = models.ManyToManyField(FinUser)

    def __str__(self):
        return f'full_name: {self.name} ticker:{self.ticker}, ' \
               f'date {self.date_update}'
