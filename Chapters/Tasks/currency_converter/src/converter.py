from api_client import CurrencyAPIClient
from storage import save_conversion

class CurrencyConverter:
    def __init__(self):
        self.client = CurrencyAPIClient()

    def convert_currency(self, amount, from_currency, to_currency):
        rate = self.client.convert(amount, from_currency, to_currency)
        save_conversion(amount, from_currency, to_currency, rate)
        return rate

    def get_currencies(self):
        return self.client.get_supported_currencies()
