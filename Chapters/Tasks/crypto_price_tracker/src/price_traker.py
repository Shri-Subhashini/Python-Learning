import requests

class CryptoPriceTracker:
    BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

    def __init__(self, coins, currency="usd"):
        self.coins = coins
        self.currency = currency
        self.alert_thresholds = {}  # e.g. {"bitcoin": 30000}

    def fetch_prices(self):
        params = {
            "ids": ','.join(self.coins),
            "vs_currencies": self.currency
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 429:
            raise Exception("Rate limit exceeded")
        response.raise_for_status()
        return response.json()

    def set_alert(self, coin, threshold_price):
        self.alert_thresholds[coin] = threshold_price

    def check_alerts(self, current_prices):
        alerts_triggered = {}
        for coin, threshold in self.alert_thresholds.items():
            price = current_prices.get(coin, {}).get(self.currency)
            if price is not None and price >= threshold:
                alerts_triggered[coin] = price
        return alerts_triggered
