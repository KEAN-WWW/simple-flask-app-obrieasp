import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_not_valid_user_content(client):
    """Test that the page for invalid user contains the correct content"""
    response = client.get("/user/invalid")
    assert response.status_code == 404  # Or another expected status code for invalid users
