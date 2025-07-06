import csv 
import os
import pytest
from src.login import validate_login

def load_login_test_data():
    test_file = os.path.join(os.path.dirname(__file__), "login_test_data.csv")
    with open(test_file, newline = "") as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            username = row['username']
            password = row['password']
            expected_success = row['expected_success'] == 'True'
            expected_error = row['expected_error'] if row["expected_error"] else None
            data.append((username, password, expected_success, expected_error))
        return data
    
@pytest.mark.parametrize("username, password, expected_success, expected_error", load_login_test_data())
def test_validate_login(username, password, expected_success, expected_error):
    result = validate_login(username.strip(), password.strip())
    assert result['success'] == expected_success
    if not expected_success:
        assert result['error'] == expected_error