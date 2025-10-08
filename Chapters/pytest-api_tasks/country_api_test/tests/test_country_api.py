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
def test_country_info(base_url, name, capital, region):
    response = requests.get(base_url)
    