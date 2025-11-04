import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def registration_user(self, email, password):
        payload = {"email": email, "password": password}
        response = self.session.post(f"{self.base_url}/register",json = payload)
        return response

    def login_user(self, email, password):
        payload = {"email": email, "password": password}
        response = self.session.post(f"{self.base_url}/login", json = payload)
        if response.status_code == 200:
            self.token = response.json().get("token")
        return response

    def get_profile(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.session.get(f"{self.base_url}/profile", headers = headers)
        return response