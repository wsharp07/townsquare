import os
import tempfile
import pytest

from townsquare.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_index_expect_200(client):
    response = client.get('/')
    assert response.status_code == 200