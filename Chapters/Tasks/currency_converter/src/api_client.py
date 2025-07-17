import requests

class CurrencyAPIClient:
    BASE_URL = "https://api.frankfurter.app"

    def get_supported_currencies(self):
        response = requests.get(f"{self.BASE_URL}/currencies")
        response.raise_for_status()
        return response.json()

    def convert(self, amount, from_currency, to_currency):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        url = f"{self.BASE_URL}/latest"
        params = {"amount": amount, "from": from_currency, "to": to_currency}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()["rates"][to_currency]
