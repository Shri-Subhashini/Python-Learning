import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from api_client import CurrencyAPIClient

@pytest.mark.testrail_case_id(3)
def test_zero_amount_conversion(mocker):
    mocker.patch("api_client.requests.get", return_value=mocker.Mock(status_code=200, json=lambda: {"rates": {"INR": 0}}))
    client = CurrencyAPIClient()
    result = client.convert(0, "USD", "INR")
    assert result == 0

@pytest.mark.testrail_case_id(4)
def test_negative_amount_raises_exception():
    client = CurrencyAPIClient()
    with pytest.raises(ValueError):
        client.convert(-10, "USD", "INR")

@pytest.mark.testrail_case_id(5)
def test_invalid_currency_code(mocker):
    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = Exception("400 Bad Request")
    mocker.patch("api_client.requests.get", return_value=mock_response)
    client = CurrencyAPIClient()
    with pytest.raises(Exception):
        client.convert(100, "USD", "INVALID")
