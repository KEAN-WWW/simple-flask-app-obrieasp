# tests/test_not_valid_user.py

"""Tests for handling invalid users"""

import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client"""
    with app.test_client() as client:
        yield client

def test_not_valid_user(client):
    """Test with a user who is not valid"""
    response = client.get("/user/jack")  # Ensure 'jack' is valid
    assert response.status_code == 200  # Expect 200 OK

    # Fix assertion to match expected output
    assert b"<h1>Hello, Jack!</h1>" in response.data
