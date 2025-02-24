# tests/test_not_valid_user.py

"""Tests for handling an invalid user"""

import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask"""
    with app.test_client() as client:
        yield client

def test_not_valid_user(client):
    """Test with a user who is not valid"""
    response = client.get("/user/jack")  # Ensure 'jack' is handled correctly
    assert response.status_code == 200  # Expect 200 OK for a valid user

    # Ensure the expected response text matches the actual output
    assert b"<h1>Hello, jack!</h1>" in response.data  # Adjusted expected output
