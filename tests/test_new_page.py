# tests/test_new_page.py
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
    assert response.status_code == 200  # Expect 200 OK status
    assert b"New Page" in response.data  # Check for content
