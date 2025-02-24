import pytest
from app.app import app  # Import your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_valid_user_content(client):
    """Test that the page for valid user contains the correct content"""
    response = client.get("/user/jack")
    assert response.status_code == 200
    assert b"Hello jack" in response.data
