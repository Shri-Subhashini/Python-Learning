import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from converter import CurrencyConverter

@pytest.mark.testrail_case_id(1)
def test_get_supported_currencies(mocker, mock_supported_currencies):
    mocker.patch("api_client.CurrencyAPIClient.get_supported_currencies", return_value=mock_supported_currencies)
    converter = CurrencyConverter()
    result = converter.get_currencies()
    assert "USD" in result
    assert result["INR"] == "Indian Rupee"

@pytest.mark.testrail_case_id(2)
def test_currency_conversion(mocker, mock_conversion_response):
    mocker.patch("api_client.CurrencyAPIClient.convert", return_value=mock_conversion_response["rates"]["INR"])
    converter = CurrencyConverter()
    rate = converter.convert_currency(100, "USD", "INR")
    assert rate == 8300.0
