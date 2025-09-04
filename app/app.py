
from flask import Flask, request, jsonify

def create_app(test_config: dict | None = None):
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)

    # Simple in-memory store (resets on restart). For the assignment this is fine.
    app.workouts = []

    @app.get("/")
    def index():
        return jsonify(message="ACEestFitness API is running", docs=["/health", "/workouts"]), 200

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    @app.post("/workouts")
    def add_workout():
        if not request.is_json:
            return jsonify(error="Expected application/json"), 415

        data = request.get_json(silent=True) or {}
        workout = (data.get("workout") or "").strip()
        duration = data.get("duration")

        if not workout:
            return jsonify(error="Field 'workout' is required"), 400

        try:
            duration = int(duration)
            if duration <= 0:
                raise ValueError
        except Exception:
            return jsonify(error="Field 'duration' must be a positive integer (minutes)"), 400

        entry = {"workout": workout, "duration": duration}
        app.workouts.append(entry)
        return jsonify(message="Workout added", entry=entry), 201

    @app.get("/workouts")
    def list_workouts():
        return jsonify(workouts=app.workouts, count=len(app.workouts)), 200

    return app

# Enable 'python -m app.app' and 'python app/app.py' for local runs
if __name__ == "__main__":
    application = create_app()
    # Use port 8000 to align with Docker/GitHub Actions checks
    application.run(host="0.0.0.0", port=8000)
