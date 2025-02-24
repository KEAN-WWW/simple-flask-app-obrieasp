import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_new_page(client):
    """Test content on the new page"""
    response = client.get("/new_page")
    assert response.status_code == 200
    assert b"New Page" in response.data
