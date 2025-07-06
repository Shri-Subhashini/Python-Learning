import csv
import requests
import pytest
import time
from concurrent.futures import ThreadPoolExecutor


url = "http://127.0.0.1:5000/login"  
# Load users from CSV
def load_users_from_csv(file_path="users.csv"):
    users = []
    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append({"username": row["username"], "password": row["password"]})
    return users

# Integration Test
# It is integration testing - becoz it involves real API, Test multiple components like (API + LOGIC +DB), No mocking of services. Calling a real API endpoint (/login). Using real HTTP request (requests.post). Sending real payload. Receiving a real response from the server. Not mocking anything — the API, app, and possibly database are all live
# This is a proper integration test because: It sends real requests to a live server. It tests full integration: input, logic, token generation, and response. It validates both success and failure scenarios.

@pytest.mark.parametrize("user", load_users_from_csv())
def test_login_api(user):
    print("Users List: ", user)  
    payload = {
        "username": user["username"],
        "password": user["password"]
    }

    response = requests.post(url, json=payload)
    json_response = response.json()

    print(f"\nTesting: {user}")
    print(f"  Status: {response.status_code}")
    print(f"  Response: {json_response}")

    # Validate successful login
    if user["username"] == "admin" and user["password"] == "secret123":
        assert response.status_code == 200
        assert "token" in json_response
    elif user["username"] == "user1" and user["password"] == "welcome":
        assert response.status_code == 200
        assert "token" in json_response
    else:
        assert response.status_code in [400, 401]
        assert "error" in json_response

# Smoke Teting 
@pytest.mark.smoke
def test_login_smoke():
    user = {"username": "admin", "password": "secret123"}
    test_login_api(user)

# Regression Testing
@pytest.mark.regression
@pytest.mark.parametrize("user", load_users_from_csv())
def test_login_regression(user):
    test_login_api(user)

# Performance Testing

@pytest.mark.performance
def test_login_performance():
    users = load_users_from_csv()
    num_threads = len(users)

    def login_and_measure(user):
        startTime = time.time()
        response = requests.post(url, json = user)
        elapsed = time.time() - startTime
        return {
            "user": user["username"],
            "status": response.status_code,
            "time": round(elapsed, 3),
            "success": "token" in response.json() if response.ok else False
        }
    with ThreadPoolExecutor(max_workers = num_threads) as executor:
        results = list(executor.map(login_and_measure, users))

    for res in results:
        print(f"\nUser: {res['user']}")
        print(f"  Status: {res['status']}")
        print(f"  Time: {res['time']}s")
        print(f"  Success: {res['success']}")

    for res in results:
        assert res['time'] < 2, f"{res['user']} took too long: {res['time']}s"