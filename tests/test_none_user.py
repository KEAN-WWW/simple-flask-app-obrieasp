# tests/test_none_user.py

"""Tests for handling a non-existent user"""

import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask"""
    with app.test_client() as client:
        yield client

def test_none_user(client):
    """Test with a user who does not exist"""
    response = client.get("/user/none")  # Request for a non-existent user
    assert response is not None, "Response is None, check the route handling."
    assert response.status_code == 404  # Expecting 404 Not Found
    assert b"User not found" in response.data  # Ensure correct error message is returned
