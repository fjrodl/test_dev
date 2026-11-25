"""Flask application Test for the CI/CD greeting."""

from app import app


def test_home():
    """Test that the home route returns the expected response."""
    response = app.test_client().get("/")

    assert response.status_code == 200  # Check for HTTP 200 status
    assert response.data == b"Hello, Flask!"  # Check the response content
