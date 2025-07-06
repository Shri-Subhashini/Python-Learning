import csv
import os
import pytest
from src.validator import is_valid_email

def read_test_data():
    test_file_path = os.path.join(os.path.dirname(__file__), "test_data.csv")
    with open(test_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['email'], row['expected'] == 'True') for row in reader]  # row['expected'] == 'True' → converts the CSV string value "True" to actual boolean True.
    return data

@pytest.mark.parametrize("email, expected", read_test_data())
def test_is_valid_email(email,expected):
    assert is_valid_email(email) == expected
