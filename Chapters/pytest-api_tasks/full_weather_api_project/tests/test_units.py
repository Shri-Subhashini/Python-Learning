import pytest
import requests

# Unit Testing for Different Measurement Units
@pytest.mark.parametrize("city,unit", [("London","metric"),("Paris","imperial")])
def test_units(base_url, api_key, city, unit):
    params = {"q": city, "appid": api_key, "units": unit}
    response = requests.get(base_url, params=params)
    assert response.status_code == 200
    data = response.json()
    temp = data["main"]["temp"]

    if unit == "metric":
        assert -100 <= temp <= 60
    elif unit == "imperial":
        assert -148 <= temp <= 140
