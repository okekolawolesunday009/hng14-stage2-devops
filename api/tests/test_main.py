# api/tests/test_main.py
from main import app
from fastapi.testclient import TestClient  # or whatever framework you're using

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_create_job():
    response = client.post("/job", json={"task": "test"})
    assert response.status_code == 200