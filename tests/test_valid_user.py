import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """Initialize a test client for Flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_valid_user_content(client):
    """Test that the page for valid user contains the correct content"""
    response = client.get("/user/jack")

    assert response.status_code == 200
    assert b"jack" in response.data
