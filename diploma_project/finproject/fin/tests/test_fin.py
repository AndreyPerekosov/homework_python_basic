from django.test import TestCase
from finauth.models import FinUser
from fin.models import Stock, Portfolio


class FInTextCase(TestCase):

    def setUp(self) -> None:
        user = FinUser.objects.create(username='ivan', password=123)
        porto = Portfolio.objects.create(name_portfolio='new', user=user)
        stock = Stock.objects.create(name='sber', ticker='sb')
        stock.portfolio.add(porto)
        stock.user.add(user)
        stock.save()

    def test_user_exists(self):
        user = FinUser.objects.get(username='ivan')
        self.assertEqual(user.username, 'ivan')

    def test_portfolio_exists(self):
        porto = Portfolio.objects.get(name_portfolio='new')
        self.assertEqual(porto.name_portfolio, 'new')

    def test_stock_exists(self):
        stock = Stock.objects.get(name='sber')
        self.assertEqual(stock.name, 'sber')

    def test_stock_porto_rel(self):
        stock = Stock.objects.get(name='sber')
        porto = stock.portfolio.all()[0]
        self.assertEqual(porto.name_portfolio, 'new')

    def test_stock_user_rel(self):
        stock = Stock.objects.get(name='sber')
        user = stock.user.all()[0]
        self.assertEqual(user.username, 'ivan')