"""This is a test script to test flask application"""
import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_not_valid_user_content(client):
    """flask unit testing for a not valid parameter page"""
    response = client.get("/user/tom")
    assert response.status_code == 200
    assert b"Anonymous" in response.data
