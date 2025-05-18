import pytest
from flask import Flask
from app import app  # Assuming the Flask app is defined in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
