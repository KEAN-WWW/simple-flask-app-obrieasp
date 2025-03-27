import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_valid_user_content(client):
    response = client.get("/user/jack")
    assert response.status_code == 200
    assert b"<h1>Hello, Jack!</h1>" in response.data
