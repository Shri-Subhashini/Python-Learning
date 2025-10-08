import requests
import pytest
from jsonschema import validate

todo_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "required": ["userId", "id", "title", "completed"]
}

# Create 
def test_create_todo(base_url):
    payload = {
        "userId": 1,
        "title": "Learn Pytest",
        "completed": False
    }

    response = requests.post(f"{base_url}/todos", json = payload)
    assert response.status_code == 201, "Status code is not 201"
    data = response.json()
    validate(instance = data, schema = todo_schema)
    assert data["title"] == payload["title"]
    assert data["completed"] is False



# Update
def test_update(base_url):
    payload = {
        "userId": 1,
        "id": 1,
        "title": "Updated Todo Title",
        "completed": True
    }

    response = requests.put(f"{base_url}/todos/1", json=payload)
    assert response.status_code == 200, "Status code is not 200"
    data = response.json()
    validate(instance=data, schema=todo_schema)
    assert data["title"] == "Updated Todo Title"
    assert data["completed"] is True

# Delete

@pytest.mark.parametrize("todo_id", [1,5,10])
def test_delete(base_url, todo_id):
    response = requests.delete(f"{base_url}/todos/{todo_id}")
    assert response.status_code in [200,204], "Status code is not 200 or 204"

# Get

def test_get(base_url):
    response = requests.get(f"{base_url}/todos")
    assert response.status_code == 200, "Status code is not 200"
    data = response.json()
    assert isinstance(data, list), "Response is not a list"
   
