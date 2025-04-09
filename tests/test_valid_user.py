"""This is a test script to test flask application"""
import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_valid_user_content(client):
    """flask unit testing for content in valid parameter page"""
    response = client.get("/user/jack")
    assert response.status_code == 200
    assert b"jack".upper() in response.data
