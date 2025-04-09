"""This is a test script to test flask application"""
import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_new_page_content(client):
    """flask unit testing for content in a route page"""
    response = client.get("/new_page")
    assert response.status_code == 200
    assert b"New Page" in response.data
