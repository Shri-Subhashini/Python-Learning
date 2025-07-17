# tests/test_weather.py

import pytest
from app.weather import fetch_weather

@pytest.mark.testrail_case_id(6)
def test_valid_city_returns_weather(patch_requests_get, valid_api_response):
    patch_requests_get.return_value.status_code = 200
    patch_requests_get.return_value.json.return_value = valid_api_response

    result = fetch_weather("London")
    print("Weather Result:", result)

    assert result["city"] == "London"
    assert result["temperature"] == 21.0
    assert result["humidity"] == 60
    assert result["description"] == "light rain"


@pytest.mark.testrail_case_id(7)
def test_empty_city_raises_value_error():
    with pytest.raises(ValueError, match="City name cannot be empty."):
        fetch_weather("")


@pytest.mark.testrail_case_id(8)
def test_404_city_not_found(patch_requests_get):
    patch_requests_get.return_value.status_code = 404
    patch_requests_get.return_value.json.return_value = {}

    result = fetch_weather("FakeCity")
    assert result["error"] == "City not found."

@pytest.mark.testrail_case_id(9)
def test_api_error_500(patch_requests_get):
    patch_requests_get.return_value.status_code = 500
    patch_requests_get.return_value.json.return_value = {}

    result = fetch_weather("New York")
    assert result["error"] == "API error."


@pytest.mark.testrail_case_id(10)
def test_network_exception(monkeypatch):
    import requests
    def raise_exception(*args, **kwargs):
        raise requests.RequestException()

    monkeypatch.setattr("app.weather.requests.get", raise_exception)

    result = fetch_weather("Berlin")
    assert result["error"] == "Network error."
