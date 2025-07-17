import json
import os

FILENAME = "frequent_conversions.json"

def save_conversion(amount, from_currency, to_currency, converted_amount):
    data = {
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
        "converted": converted_amount,
    }
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            all_data = json.load(file)
    else:
        all_data = []

    all_data.append(data)

    with open(FILENAME, "w") as file:
        json.dump(all_data, file, indent=2)

def load_conversions():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)
