import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """Initialize a fixture test client for Flask unit testing."""
    with app.test_client() as app_client:
        yield app_client

def test_none_user_content(client):
    """Flask unit testing for an unreachable page when the parameter is missing."""
    response = client.get("/user/")
    assert response.status_code == 404

    # Check if the response contains part of the expected error page content
    assert b"Not Found" in response.data
