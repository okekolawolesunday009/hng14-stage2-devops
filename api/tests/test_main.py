# api/tests/test_main.py
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


@patch("main.r")
def test_create_job_returns_200(mock_redis):
    mock_redis.lpush = MagicMock(return_value=1)
    mock_redis.hset = MagicMock(return_value=1)

    response = client.post("/jobs")
    assert response.status_code == 200


@patch("main.r")
def test_create_job_returns_job_id(mock_redis):
    mock_redis.lpush = MagicMock(return_value=1)
    mock_redis.hset = MagicMock(return_value=1)

    response = client.post("/jobs")
    assert "job_id" in response.json()
    assert len(response.json()["job_id"]) > 0


@patch("main.r")
def test_get_job_status(mock_redis):
    mock_redis.hget = MagicMock(return_value=b"queued")

    response = client.get("/jobs/abc123")
    assert response.status_code == 200
    assert response.json()["status"] == "queued"
    assert response.json()["job_id"] == "abc123"
