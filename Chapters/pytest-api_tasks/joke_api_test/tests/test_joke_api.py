import requests
import pytest
# from jsonschema import validate

# json_schema = {
#     "type": "object",
#     "properties" :{
#         "id": {"type": "integer"},
#         "type": {"type":"string"},
#         "setup":{"type":"string"},
#         "punchline":{"type":"string"}
#     },

#     "required": ["id", "type", "setup", "punchline"]
# }


# Validate Random Joke endpoint

def test_get_random_joke(base_url):
    response = requests.get(f"{base_url}/random_joke")
    assert response.status_code == 200, "Status code is not 200"
    json_data = response.json()
    # validate(instance = json_data, schema = json_schema)
    assert "setup" in json_data, "Joke field is missing"
    assert len(json_data["setup"]) > 0, "Joke is empty"


#Parameterized test for multiple endpoints

@pytest.mark.parametrize("endpoint", ["/random_ten", "/random_joke"])
def test_multiple_endpoints(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    assert response.status_code == 200, f"Status code for {endpoint} is not 200"
    assert response.headers["Content-Type"].startswith("application/json")
