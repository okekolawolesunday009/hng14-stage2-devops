# api/tests/test_main.py
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


@patch("main.r")
def test_create_job(mock_redis):
    mock_redis.lpush = MagicMock(return_value=1)
    mock_redis.hset = MagicMock(return_value=1)

    response = client.post("/jobs", json={"name": "test"})
    assert response.status_code == 200
    assert "id" in response.json()


@patch("main.r")
def test_create_job_returns_job_id(mock_redis):
    mock_redis.lpush = MagicMock(return_value=1)
    mock_redis.hset = MagicMock(return_value=1)

    response = client.post("/jobs", json={"name": "test"})
    job_id = response.json().get("id")
    assert job_id is not None
    assert len(job_id) > 0


@patch("main.r")
def test_get_job_status(mock_redis):
    mock_redis.hgetall = MagicMock(return_value={
        b"id": b"abc123",
        b"name": b"test",
        b"status": b"pending"
    })

    response = client.get("/jobs/abc123")
    assert response.status_code == 200
    assert response.json()["status"] == "pending"
