import pytest
import requests


# City/Location Tests
@pytest.mark.parametrize("city,expected_status,unit", [
    ("London",200,"metric"),
    ("Paris",200,"metric"),
    ("Tokyo",200,"metric"),
    ("",400,"metric"),
    ("@!#$%^",404,"metric"),
    ("AReallyLongCityNameExceedingNormalLimits",404,"metric")
])
def test_city_validations(base_url, api_key, city, expected_status, unit):
    params = {"q": city, "appid": api_key, "units": unit}
    response = requests.get(base_url, params=params)
    assert response.status_code == expected_status
