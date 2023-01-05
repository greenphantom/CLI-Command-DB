"""Script defining the utility for generating a client for testing route endpoints."""

import pytest
from flaskr import create_app


@pytest.fixture
def client():
    """Pytest fixture to reuse for route unit testing of web routing."""
    application = create_app()

    with application.test_client() as client:
        with application.app_context():
            yield client
