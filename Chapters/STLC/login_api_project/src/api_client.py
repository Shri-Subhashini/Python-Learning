import requests

def login_api(username: str, password: str) -> dict:

    url = "https://example.com/api/login"
    response = requests.post(url, json = {'username': username, 'password': password})
    response.raise_for_status()
    return response.json()
    
