from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_chat_api():
    response = client.post("/chat", json={"message": "do you provide placement assistance"})
    assert response.status_code == 200
    assert "response" in response.json()

