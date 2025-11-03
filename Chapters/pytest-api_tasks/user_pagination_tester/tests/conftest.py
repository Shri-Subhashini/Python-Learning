import pytest
import requests
import os
import json

@pytest.fixture(scope = "session")
def base_url():
    return "https://reqres.in/api/users"

@pytest.fixture(scope = "session")
def load_user_schema():
    schema_path = os.path.join(os.path.dirname(__file__), "schemas", "user_list_schema.json")
    with open(schema_path, "r") as file:
        return json.load(file)

@pytest.fixture(scope = "session")
def get_page_data(base_url):
    def _get_page(page_number):
        response = requests.get(base_url, params = {"page": page_number})
        return response
    return _get_page
