"""This is a test script to test flask application"""
import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_none_user_content(client):
    """flask unit testing for unreachable page if a parameter is missing"""
    response = client.get("/user/")
    assert response.status_code == 404