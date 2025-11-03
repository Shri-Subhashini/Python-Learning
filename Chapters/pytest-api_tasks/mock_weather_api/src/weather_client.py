import requests

class WeatherClient:
    def __init__(self,base_url):
        self.base_url = base_url

    def get_weather(self, city):
        url = f"{self.base_url}/weather?q={city}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error":"City not found"}
        elif response.status_code == 500:
            return {"error": "Internal server error"}
        else:
            return {"error": f"Unexpected status {response.status_code}"}


            