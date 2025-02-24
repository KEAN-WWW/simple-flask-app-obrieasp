# tests/test_valid_user.py
"""Tests for validating user page content"""
import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask"""
    with app.test_client() as client:
        yield client

def test_valid_user_content(client):
    """Test that the page for a valid user contains the correct content"""
    response = client.get("/user/jack")  # Ensure 'jack' is a valid user
    assert response.status_code == 200  # Expect 200 OK status

    # Update the assertion to match the actual response content
    assert b"<h1>Hello, Jack!</h1>" in response.data
