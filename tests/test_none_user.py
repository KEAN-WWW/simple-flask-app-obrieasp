import pytest
from app.app import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to create a test client for Flask"""
    with app.test_client() as client:
        yield client

def test_none_user(client):
    """Test with a user who does not exist"""
    response = client.get("/user/none")
    assert response.status_code == 404  # Expecting 404 for non-existent user
