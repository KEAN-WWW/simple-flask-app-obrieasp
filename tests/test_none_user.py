import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_none_user_content(client):
    """Test that a nonexistent user shows a proper error message"""
    response = client.get("/user/none")
    assert response.status_code == 404  # Adjust based on expected behavior
