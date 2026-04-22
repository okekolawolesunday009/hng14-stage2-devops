# api/tests/test_main.py
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_job():
    response = client.post("/job", json={"name": "test"})
    assert response.status_code == 200
