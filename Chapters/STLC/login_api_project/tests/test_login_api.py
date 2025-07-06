import csv 
import json
import os
import pytest
from unittest.mock import patch, Mock
from src.api_client import login_api

def load_csv_data():
    test_file = os.path.join(os.path.dirname(__file__), "login_api_data.csv")
    with open(test_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        test_data = []
        for row in reader:
            test_data.append(
                (row["username"], row["password"], int(row["status_code"]), row["response_body"])
            )
        return test_data
    
@pytest.mark.parametrize("username, password, status_code, response_body", load_csv_data())
@patch("src.api_client.requests.post")
def test_login_api(mock_post, username, password, status_code, response_body):
    mock_response = Mock()  # Creates a fake response object.
    mock_response.status_code = status_code
    mock_response.json.return_value = json.loads(response_body) if response_body.startswith("{") else {}
    
    mock_post.return_value = mock_response

    if status_code >= 400:
        mock_response.raise_for_status.side_effect = Exception(response_body)
    else:
        mock_response.raise_for_status.return_value = None

    if status_code >= 400:
        with pytest.raises(Exception) as excinfo:
            login_api(username, password)
        assert response_body in str(excinfo.value)
    else:
        result = login_api(username, password)
        assert result == mock_response.json.return_value