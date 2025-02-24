import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask"""
    with app.test_client() as client:
        yield client

def test_main_page_content(client):
    """Test content on the main page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Main Page!" in response.data
