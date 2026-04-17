from etl.preprocess import clean_text

def test_clean_text():
    text = "Do YOU provide Placement Support???"
    result = clean_text(text)

    assert "provide" in result
    assert "placement" in result