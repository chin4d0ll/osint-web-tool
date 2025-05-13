import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_social_footprint(client):
    response = client.post(
        "/api/social_footprint", json={"platform": "twitter", "username": "testuser"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "result" in data
    assert data["result"]["platform"] == "twitter"
    assert data["result"]["username"] == "testuser"


def test_risk_assessment(client):
    response = client.post("/api/risk_assessment", json={"target": "testuser"})
    assert response.status_code == 200
    data = response.get_json()
    assert "result" in data
    assert data["result"]["target"] == "testuser"


def test_commercial_api(client):
    response = client.post(
        "/api/commercial", json={"query": "test"}, headers={"x-api-key": "demo-key"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "result" in data
    assert data["result"]["query"] == "test"


def test_commercial_api_no_key(client):
    response = client.post("/api/commercial", json={"query": "test"})
    assert response.status_code == 401
