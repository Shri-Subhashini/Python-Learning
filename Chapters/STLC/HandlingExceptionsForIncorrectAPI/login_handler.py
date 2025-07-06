import requests

def login_user(api_url, payload):
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error: {http_err}"}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection failed: Endpoint not reachable."}
    except requests.exceptions.Timeout:
        return {"error": "Request timed out."}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}
