import pytest
import requests

#Authentication
def test_valid_token(base_url, api_key, default_city):
    params = {"q": default_city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params = params)
    # print(f" Response : {response}")
    assert response.status_code == 200, "Expected 200 OK for valid API key"
    data = response.json()

    assert "main" in data, "Response should contain 'main' key"
    assert "temp" in data["main"], "Response 'main' should contain 'temp' key"
    print(f"{default_city}: {data["main"]["temp"]}°C")


def test_invalid_token(base_url, default_city):
    invalid_api = "INVALID API KEY"
    params = {"q": default_city, "appid": invalid_api}
    response = requests.get(base_url, params = params)

    assert response.status_code == 401, "Expected 401 Unauthorized for invalid API key"

# https://api.openweathermap.org/data/2.5/weather?q=London&appid=d94641798a0dd52105e576cc29695d39&units=metrics


# Data Driven Tests

@pytest.mark.parametrize("city, expected_status", [("London",200), ("Paris",200),("Tokyo",200),
                          ("New York",200),("Mumbai",200),
                          ("InvalidCity1",404),("InvalidCity2",404) ])
def test_city_weather_status(base_url, api_key, city, expected_status):
    params = {"q": city, "appid": api_key, "units": "metrics"}
    response =  requests.get(base_url, params = params)
    assert response.status_code == expected_status, f"Expected {expected_status} for city {city}"

    if response.status_code == 200:
        data = response.json()
        assert "main" in data, f"{city}: Response missing 'main'"
        assert "temp" in data["main"], f"{city}: Response missing 'temp'"
        assert isinstance(data['main']['temp'], (float, int)), f"{city}: Temperature is not a number"
