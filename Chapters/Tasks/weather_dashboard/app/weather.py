import requests

API_KEY = "12487f350b9b7ffc256e25ded428151e"

BASE_URL = "https://api.openweathermap.org/data/2.5"


def fetch_weather(city_name):
    if not city_name or not city_name.strip():
        raise ValueError("City name cannot be empty.")

    try:
        url = f"{BASE_URL}/weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
    except requests.RequestException:
        return {"error": "Network error."}

    if response.status_code == 404:
        return {"error": "City not found."}
    elif response.status_code != 200:
        return {"error": "API error."}

    data = response.json()
    return {
        "city": data.get("name"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }   