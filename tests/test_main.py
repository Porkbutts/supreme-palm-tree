"""Test module"""
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_read_main():
    """test_read_main"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
