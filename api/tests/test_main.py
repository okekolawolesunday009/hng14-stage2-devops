# api/tests/test_main.py
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health():                                    # E302: two blank lines before top-level function
    response = client.get("/health")
    assert response.status_code == 200


def test_create_job():
    response = client.post("/job", json={"task": "test"})
    assert response.status_code == 200
                                                      # W292: newline at end of file