import pytest
import requests
import json
import os

@pytest.fixture(scope = "session")
def base_url():
    return "https://fakerapi.it/api/v1/books"


@pytest.fixture(scope = "session")
def get_books(base_url):
    response =  requests.get(base_url, params = {"_quantity":3})
    assert response.status_code == 200
    return response.json()


@pytest.fixture(scope = "session")
def load_book_schema():
    schema_path = os.path.join(os.path.dirname(__file__), "schemas", "book_schema.json")
    with open(schema_path, "r") as file:
        return json.load(file)


 