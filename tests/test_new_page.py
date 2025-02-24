import pytest
from app.app import app

@pytest.fixture(name="client")
def create_client():
    """Initialize a fixture test client for Flask unit testing."""
    with app.test_client() as app_client:
        yield app_client  # Provide the test client to tests

def test_new_page_content(client):
    """Flask unit testing for content in the /new_page route."""
    response = client.get("/new_page")  # Sending GET request for the new page
    assert response.status_code == 200  # Assert that the response status code is 200

    # Check if the page contains "New Page" in its content
    assert b"New Page" in response.data

    # Optionally, check for specific elements or additional text
    assert b"<h1>New Page</h1>" in response.data  # Ensure the page contains an <h1> tag with "New Page"
