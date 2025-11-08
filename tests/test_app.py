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

def test_add_workout_with_category(client):
    payload = {"category": "Warm-up", "workout": "Stretching", "duration": 10}
    rv = client.post("/workouts", data=json.dumps(payload), content_type="application/json")
    assert rv.status_code == 201
    data = rv.get_json()
    assert data["entry"]["exercise"] == "Stretching"
    assert data["category"] == "Warm-up"

def test_add_and_list_workouts(client):
    rv = client.get("/workouts")
    assert rv.status_code == 200
    assert rv.get_json()["count"] == 0

    payload = {"workout": "Running", "duration": 30}
    rv = client.post("/workouts", data=json.dumps(payload), content_type="application/json")
    assert rv.status_code == 201
    data = rv.get_json()
    assert data["entry"]["exercise"] == "Running"
    assert data["entry"]["duration"] == 30

    rv = client.get("/workouts")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["count"] == 1

def test_summary_endpoint(client):
    payload = {"category": "Workout", "workout": "Running", "duration": 45}
    client.post("/workouts", json=payload)
    
    rv = client.get("/summary")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["total_time"] == 45
    assert "motivation" in data

def test_workout_chart_endpoint(client):
    rv = client.get("/workout-chart")
    assert rv.status_code == 200
    data = rv.get_json()
    assert "workout_chart" in data
    assert "Warm-up" in data["workout_chart"]
    assert "Workout" in data["workout_chart"]
    assert "Cool-down" in data["workout_chart"]

def test_diet_chart_endpoint(client):
    rv = client.get("/diet-chart")
    assert rv.status_code == 200
    data = rv.get_json()
    assert "diet_plans" in data
    assert "Weight Loss" in data["diet_plans"]
    assert "Muscle Gain" in data["diet_plans"]
    assert "Endurance" in data["diet_plans"]

def test_progress_endpoint(client):
    rv = client.get("/progress")
    assert rv.status_code == 200
    data = rv.get_json()
    assert "totals" in data
    assert "percentages" in data
    assert "total_time" in data

def test_invalid_category(client):
    payload = {"category": "Invalid", "workout": "Test", "duration": 10}
    rv = client.post("/workouts", json=payload)
    assert rv.status_code == 400

def test_validation_errors(client):
    rv = client.post("/workouts", data="not-json", content_type="text/plain")
    assert rv.status_code == 415

    rv = client.post("/workouts", json={"duration": 10})
    assert rv.status_code == 400
    
    rv = client.post("/workouts", json={"workout": "X"})
    assert rv.status_code == 400

    rv = client.post("/workouts", json={"workout": "X", "duration": -5})
    assert rv.status_code == 400
    
    rv = client.post("/workouts", json={"workout": "X", "duration": "abc"})
    assert rv.status_code == 400
