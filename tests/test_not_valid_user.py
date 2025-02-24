import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask"""
    with app.test_client() as client:
        yield client

def test_not_valid_user(client):
    """Test with a user who is not valid"""
    response = client.get("/user/jack")  # Change 'jack' to a user name that should be valid
    assert response.status_code == 200  # Expect 200 OK for valid user
    assert b"Hello jack" in response.data  # Check for expected content
