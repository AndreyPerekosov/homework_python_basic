from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return f'name: {self.name} email:{self.email}'


class Portfolio(models.Model):
    name_portfolio = models.CharField(max_length=200)
    data = models.JSONField(null=True)
    date_update = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'full_name: {self.name_portfolio} tick:{data}, ' \
               f'date: {self.date_update}'


class Stock(models.Model):
    full_name = models.CharField(max_length=200)
    tick = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    date_update = models.DateField(auto_now=True)
    desc = models.TextField(blank=True)
    portfolio = models.ManyToManyField(Portfolio)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f'full_name: {self.full_name} tick:{self.tick}, ' \
               f'date {self.date_update}'
