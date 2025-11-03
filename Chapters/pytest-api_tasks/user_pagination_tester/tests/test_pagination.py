import pytest
import requests
import os
from jsonschema import validate
from jsonschema.exceptions import ValidationError



# Checking status code of the API response
def test_api_status_code(get_page_data):
    response = get_page_data(2)
    assert response.status_code == 200

# Validating user schema
def test_validate_schema(get_page_data, load_user_schema):
    response = get_page_data(2).json()
    validate(instance = response, schema = load_user_schema)


# Testing metadata of pagination
def test_pagination_metadata(get_page_data):
    response = get_page_data(2).json()
    assert response["page"] == 2
    assert response["per_page"] == 6
    assert response["total"] == 12
    assert response["data"][0]["email"] == "michael.lawson@reqres.in"


# Testing that user fields are not empty
def test_user_field_not_empty(get_page_data):
    response = get_page_data(2).json()
    for user in response["data"]:
        assert all(k in user for k in ["id", "email", "first_name", "last_name", "avatar"])
        assert all(user[k] for k in ["id", "email", "first_name", "last_name", "avatar"])
        assert ("id" in user)
    
# Validate all emails have '@' symbol
def test_email_format(get_page_data):
    response = get_page_data(2).json()
    for user in response["data"]:
        assert "@" in user["email"], f"Invalid email format: {user['email']}"

# Testing that data on different pages is not the same
def test_pagination_data_differs(get_page_data):
    page1 = get_page_data(1).json()["data"]
    page2 = get_page_data(2).json()["data"]
    assert page1 != page2, "Data on page 1 and page 2 should differ" 

# Validate total pages and total users consistency
def test_total_page_consistency(get_page_data):
    response = get_page_data(2).json()
    expected_total = response["per_page"] * response["total_pages"]
    assert response["total"] == expected_total, "Total users count mismatch"


# Validating response for invalid page number
def test_invalid_page_number(get_page_data):
    response = get_page_data(1000).json()
    data = response.get("data", [])
    assert data == [], "Expected empty data for non-existent page"

# Validate unique user ids across pages
def test_unique_user_ids(get_page_data):
    ids = []
    for page in [1, 2]:
        response = get_page_data(page).json()
        for user in response["data"]:
            ids.append(user["id"])
    assert len(ids) == len(set(ids)), "User IDs are not unique across pages"         


# Test filtering by per_page parameter
# @pytest.mark.parametrize("per_page", [3, 4, 5])
# def test_per_page_filter(get_page_data, per_page):
#     response = get_page_data(1)  # Returns response objects like response.json(), response.status_code, response.headers, response.url
#     print(f"Response : {response}")
#     data = requests.get(response.url, params = {"per_page": per_page}).json()
#     # assert len(data["data"]) ==  per_page, f"Expected {per_page} users per page"
#     assert "data" in data, "Response does not contain 'data' key"
#     assert len(data["data"]) <= per_page, f"Expected at most {per_page} users per page"
#     print(f"per_page={per_page}, users returned: {len(data['data'])}")

