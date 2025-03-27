import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_none_user(client):
    response = client.get("/user/none")
    assert response is not None, "Response is None, check the route handling."
    assert response.status_code == 404
    assert b"User not found" in response.data
