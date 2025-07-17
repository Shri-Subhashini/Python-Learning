def test_alert_trigger(sample_tracker, mock_success_response):
    tracker = sample_tracker
    tracker.set_alert("bitcoin", 30000)
    tracker.set_alert("ethereum", 2500)  # won't trigger
    prices = tracker.fetch_prices()

    alerts = tracker.check_alerts(prices)
    assert "bitcoin" in alerts
    assert alerts["bitcoin"] == 31000
    assert "ethereum" not in alerts
