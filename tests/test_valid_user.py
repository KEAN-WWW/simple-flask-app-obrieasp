# tests/test_valid_user.py
import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client"""
    with app.test_client() as client:
        yield client

def test_valid_user_content(client):
    """Test that the page for valid user contains the correct content"""
    response = client.get("/user/jack")  # Ensure 'jack' is a valid user in your logic
    assert response.status_code == 200  # Expect 200 OK status
    assert b"Hello, jack!" in response.data  # Check for expected content (note the comma)
