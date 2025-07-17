def test_fetch_prices_parsing(sample_tracker, mock_success_response):
    prices = sample_tracker.fetch_prices()
    assert prices["bitcoin"]["usd"] == 31000
    assert prices["ethereum"]["usd"] == 2100
    assert prices["dogecoin"]["usd"] == 0.08
