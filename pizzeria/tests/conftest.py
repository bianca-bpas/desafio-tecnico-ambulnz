import pytest
from fastapi.testclient import TestClient

from pizzeria.app import app


@pytest.fixture
def client():
    return TestClient(app)
