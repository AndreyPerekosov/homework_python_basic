from django.db import models
from finauth.models import FinUser


class Portfolio(models.Model):
    name_portfolio = models.CharField(max_length=200)
    date_update = models.DateField(auto_now=True)
    data = models.TextField(blank=True)
    colors = models.TextField(blank=True)
    user = models.ForeignKey(FinUser, on_delete=models.CASCADE)
    volatility = models.FloatField(null=True)
    portfolio_return = models.FloatField(null=True)
    sharp = models.FloatField(null=True)

    def __str__(self):
        return f'portfolio_name: {self.name_portfolio}, data:{self.data} ', \
               f'portfolio return: {self.portfolio_return} ', \
               f'volatility: {self.volatility} ', \
               f'sharp: {self.sharp} ', \
               f'date of update: {self.date_update}' , \
               f'owner: {self.user}'


class Stock(models.Model):
    figi = models.CharField(max_length=50, blank=True)
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
        return f'name: {self.name} ticker:{self.ticker}, ' \
               f'date {self.date_update}'
