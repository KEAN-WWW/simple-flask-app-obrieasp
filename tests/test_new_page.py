# tests/test_new_page.py

"""Test for the new page content"""

import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client"""
    with app.test_client() as client:
        yield client

def test_new_page_content(client):
    """Test the content on the new page"""
    response = client.get("/new")
    assert response.status_code == 200
    assert b"Welcome to the New Page!" in response.data
