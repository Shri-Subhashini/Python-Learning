import pytest
import requests


# Weather Data Validation Tests
def test_weather_data_ranges(base_url, api_key, default_city):
    params = {"q": default_city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    assert -100 <= temp <= 60, f"Temp {temp} out of range"
    assert 0 <= humidity <= 100, f"Humidity {humidity} out of range"
    assert wind_speed >= 0, f"Wind speed {wind_speed} should be >= 0"
