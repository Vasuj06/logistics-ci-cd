import json
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["status"] == "Running"

def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200