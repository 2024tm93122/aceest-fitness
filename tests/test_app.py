
import json
import pytest
from app.app import create_app

@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_health_ok(client):
    rv = client.get("/health")
    assert rv.status_code == 200
    assert rv.get_json()["status"] == "ok"

def test_add_and_list_workouts(client):
    # initially empty
    rv = client.get("/workouts")
    assert rv.status_code == 200
    assert rv.get_json()["count"] == 0

    # add one
    payload = {"workout": "Running", "duration": 30}
    rv = client.post("/workouts", data=json.dumps(payload), content_type="application/json")
    assert rv.status_code == 201
    data = rv.get_json()
    assert data["entry"]["workout"] == "Running"
    assert data["entry"]["duration"] == 30

    # list again
    rv = client.get("/workouts")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["count"] == 1
    assert data["workouts"][0]["workout"] == "Running"
    assert data["workouts"][0]["duration"] == 30

def test_validation_errors(client):
    # missing json
    rv = client.post("/workouts", data="not-json", content_type="text/plain")
    assert rv.status_code == 415

    # missing fields
    rv = client.post("/workouts", json={"duration": 10})
    assert rv.status_code == 400
    rv = client.post("/workouts", json={"workout": "X"})
    assert rv.status_code == 400

    # bad duration
    rv = client.post("/workouts", json={"workout": "X", "duration": -5})
    assert rv.status_code == 400
    rv = client.post("/workouts", json={"workout": "X", "duration": "abc"})
    assert rv.status_code == 400
