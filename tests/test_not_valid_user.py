import pytest
from app.app import app  # Import the Flask app

@pytest.fixture(name="client")
def create_client():
    """Initialize a fixture test client for Flask unit testing."""
    with app.test_client() as app_client:
        yield app_client

def test_not_valid_user_content(client):
    """Flask unit testing for a non-valid username page."""
    response = client.get("/user/tom")
    assert response.status_code == 200
    assert b"Anonymous" in response.data
