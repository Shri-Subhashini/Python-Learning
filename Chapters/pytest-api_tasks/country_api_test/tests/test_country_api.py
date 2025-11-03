import pytest
import requests
import csv

def load_test_data():
    data = []
    with open("data/countries.csv", newline = '', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((row["name"], row["capital"], row["region"]))
    return data

@pytest.mark.parametrize("name,capital,region", load_test_data())
def test_country_info(all_countries, name, capital, region):
    countries = all_countries
    match = next((c for c in countries if c["name"]["common"].lower() == name.lower()), None)
    assert match is not None, f"Country {name} not found"
    print(f"match: {match}")

    actual_capital = match.get("capital", ["N/A"])[0]   # dict.get(key, default_value) ; [0] -> the value of "capital" is a list, not a string.
    actual_region = match.get("region", "N/A")

    assert actual_capital.lower() == capital.lower(), f"Expected capital {capital}, got {actual_capital}"
    assert actual_region.lower() == region.lower(), f"Expected region {region}, got {actual_region}"
