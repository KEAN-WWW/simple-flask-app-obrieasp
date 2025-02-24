# tests/test_new_page.py

"""Tests for the new page route"""

import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask"""
    with app.test_client() as client:
        yield client

def test_new_page_content(client):
    """Test the content on the new page"""
    response = client.get("/new")
    assert response.status_code == 200
    assert b"<h1>New Page</h1>" in response.data  # Updated expected content
