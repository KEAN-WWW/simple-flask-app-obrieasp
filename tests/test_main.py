# tests/test_main.py

"""Tests for the main application routes"""

import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask"""
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Home Page" in response.data  # Ensure expected content
