import requests
import json

import telebot.types

from config import keys


class ConvertExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(message: telebot.types.Message, quote: str, base: str, amount: str):
        value = message.text.split()
        quote, base, amount = value

        if len(value) != 3:
            raise ConvertExeption('Введите три параметра.')

        if quote == base:
            raise ConvertExeption(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker == keys[quote]
        except KeyError:
            raise ConvertExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker == keys[base]
        except KeyError:
            raise ConvertExeption(f'Не удалось обработать валюту {base}')

        try:
            amount == float(amount)
        except ValueError:
            raise ConvertExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base, amount
