import pytest
import requests
from jsonschema import validate, ValidateError

# Validate status code
def test_api_status_code(get_bookstore_api):
    assert get_bookstore_api["code"] == 200, "API did not return status code 200"

def test_json_schema_validation(get_bookstore_api, load):
    validate(instance = get_bookstore_api, schema = load_book_schema)


def test_book_fields_not_empty(get_bookstore_api):
    for book in get_bookstore_api["data"]:
        assert book["title"], "Book title is empty"
        assert book["author"], "Book author is empty"
        assert book["isbn"], "Book ISBN is empty"

        

