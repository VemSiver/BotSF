import requests
import json

from Config import keys


class ConvertionsException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionsException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionsException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionsException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionsException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={quote_ticker}{base_ticker}&key=e5ae24a97043df1f645743f003209bad')
        total_base = json.loads(r.content)

        return total_base