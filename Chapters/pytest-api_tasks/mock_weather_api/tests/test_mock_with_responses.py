import pytest
import responses
import requests

# Successful mock response
@responses.activate
def test_successful_weather_response(weather_client):
    mock_url = f"{weather_client.base_url}/weather?q=London"
    mock_json = {"city": "London", "temperature": 25, "unit": "Celsius"}

    responses.add(responses.GET, mock_url, json=mock_json, status = 200)

    response = weather_client.get_weather("London")
    assert response["city"] == "London"
    assert response["temperature"] == 25
    assert response["unit"] == "Celsius"

# Mock 404 city not found

def test_city_not_found(weather_client):
    mock_url = f"{weather_client.base_url}/weather?q=UnknownCity"
    responses.add(response.GET, mock_url, json = {"error": "City not found"}, status = 404)
    response = weather_client.get_weather("UnknownCity")
    assert response["error"] == "City not found"
    

# Mock 500 internal server error

@responses.activate
def test_internal_server_error(weather_client):
    mock_url = f"{weather_client.base_url}/weather?q=Paris"
    responses.add(responses.GET, mock_url, json = {"error": "Internal Server Error"}, status = 500)
    response = weather_client.get_weather("Paris")
    assert response["error"] == "Internal server error"


# Mock unexpected status(418)

@responses.activate
def test_unexpected_status(weather_client):
    mock_url = f"{weather_client.base_url}/weather?q=Berlin"
    responses.add(responses.GET, mock_url, json = {}, status = 418)

    response = weather_client.get_weather("Berlin")
    assert "Unexpected status" in response["error"]


# Stimulate timeout / connection error

@responses.activate
def test_connection_server(weather_client):
    mock_url = f"{weather_client.base_url}/weather?q=Rome"

    def raise_error(request):
        raise requests.exceptions.ConnectionError("Network timeout")
    
    responses.add_callback(responses.GET, mock_url, callback = raise_error)

    with pytest.raises(requests.exceptions.ConnectionError):
        weather_client.get_weather("Rome")