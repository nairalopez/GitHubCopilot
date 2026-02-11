import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Get an activity name
    activities = client.get("/activities").json()
    activity_name = next(iter(activities))
    email = "testuser@mergington.edu"

    # Sign up
    signup_url = f"/activities/{activity_name}/signup?email={email}"
    response = client.post(signup_url)
    assert response.status_code == 200
    assert "message" in response.json()

    # Unregister
    unregister_url = f"/activities/{activity_name}/unregister?email={email}"
    response = client.post(unregister_url)
    assert response.status_code == 200
    assert "message" in response.json()
