from django.core.management import BaseCommand
from fin.models import Stock
from dataclasses import dataclass
import json

@dataclass
class DataInstruments:
    figi: str
    ticker: str
    lot: int
    currency: str
    name: str


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('data/data_file.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            data_classes = []
            for item in data['payload']['instruments']:
                tmp = DataInstruments(
                    item['figi'], item['ticker'],
                    item['lot'], item['currency'], item['name']
                                    )
                data_classes.append(tmp)
            for item in data_classes:
                Stock.objects.create(
                    name=item.name, ticker=item.ticker,
                    lot=item.lot, currency=item.currency, figi=item.figi
                                     )
