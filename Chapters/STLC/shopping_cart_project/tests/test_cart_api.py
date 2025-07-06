import csv
import json
import os
import pytest
from unittest.mock import patch, Mock
from src import cart_api

def load_csv_data(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
    
@pytest.mark.parametrize("row", load_csv_data("cart_test_add.csv"))
@patch("src.cart_api.requests.post")
def test_add_to_cart(mock_post, row):
    mock_response = Mock()
    mock_response.status_code = int(row["status_code"])
    mock_response.json.return_value = json.loads(row["response_json"])
    
    if mock_response.status_code >= 400:
        mock_response.raise_for_status.side_effect = Exception(row["response_json"])
    else:
        mock_response.raise_for_status.return_value = None

    mock_post.return_value = mock_response

    try:
        result = cart_api.add_to_cart(int(row["product_id"]), int(row["quantity"]))
        assert isinstance(result, dict)
    except Exception as e:
        error = json.loads(str(e))
        assert "error" in error


@pytest.mark.parametrize("row", load_csv_data("cart_test_remove.csv"))
@patch("src.cart_api.requests.post")
def test_remove_from_cart(mock_post, row):
    mock_response = Mock()
    mock_response.status_code = int(row["status_code"])
    mock_response.json.return_value = json.loads(row["response_json"])

    if mock_response.status_code >= 400:
        mock_response.raise_for_status.side_effect = Exception(row["response_json"])
    else:
        mock_response.raise_for_status.return_value = None

    mock_post.return_value = mock_response

    try:
        result = cart_api.remove_from_cart(int(row["product_id"]))
        assert isinstance(result, dict)
    except Exception as e:
        error = json.loads(str(e))
        assert "error" in error



@pytest.mark.parametrize("row", load_csv_data("cart_test_view.csv"))
@patch("src.cart_api.requests.get")
def test_view_cart(mock_get, row):
    mock_response = Mock()
    mock_response.status_code = int(row["status_code"])
    mock_response.json.return_value = json.loads(row["response_json"])

    if mock_response.status_code >= 400:
        print("Raw JSON string:", row["response_json"])
        mock_response.raise_for_status.side_effect = Exception(row["response_json"])
    else:
        mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    try:
        result = cart_api.view_cart()
        assert isinstance(result, dict)
    except Exception as e:
        error = json.loads(str(e))
        assert "error" in error
