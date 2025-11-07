# ACEest Fitness & Gym — Introduction To DevOps Assignment 1 Solution

# A minimal Flask API that models basic workout logging for **ACEest_Fitness and Gym**, packaged with unit tests, Dockerfile, and a GitHub Actions CI pipeline.

## Project Layout

```text
.
├── app/
│   ├── __init__.py
│   ├── app.py            # Flask app (app factory: create_app())
│   └── templates/        # HTML templates
│       └── index.html    # Web UI interface
├── tests/
│   ├── conftest.py       # Test configuration
│   └── test_app.py       # Pytest unit tests
├── .github/workflows/
│   └── CI.yml            # GitHub Actions pipeline
├── ACEest_Fitness.py     # Original Tkinter app
├── Dockerfile
├── requirements.txt
└── README.md
```

## 1) Run Locally (No Docker)

**Prereqs:** Python 3.11+

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Start the app on http://localhost:8000
python -m app.app
```

**Try it:**

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/workouts -H "Content-Type: application/json" -d '{"workout":"Running","duration":30}'
curl http://localhost:8000/workouts

# Add a workout
curl -X POST http://localhost:8000/workouts \
  -H "Content-Type: application/json" \
  -d '{"category":"Workout","workout":"Running","duration":30}'

# Get all workouts
curl http://localhost:8000/workouts

# Get summary
curl http://localhost:8000/summary

# Get workout recommendations
curl http://localhost:8000/workout-chart

# Get diet plans
curl http://localhost:8000/diet-chart

# Get progress data
curl http://localhost:8000/progress
```

**Run unit tests:**

```bash
pytest -q
```

## 2) Run with Docker

```bash
docker build -t aceest-fitness:local .
docker run -p 8000:8000 aceest-fitness:local
```

## 3) Git & GitHub (Suggested Workflow)

```bash
git init
git add .
git commit -m "feat: initial Flask app, tests, Dockerfile, CI"
git branch -M main
git remote add origin https://github.com/2024tm93122/aceest-fitness.git
git push -u origin main
```

Pushes to GitHub will trigger the **CI workflow**:

- Install deps and run **pytest**
- Build Docker image and run a **smoke test** (health check + sample API calls)

## 4) Web UI

After starting the app, visit the web interface:
```bash
# Open in browser
http://localhost:8000/ui
```

The UI provides:
- Dashboard with workout stats
- Form to add new workouts
- List of all logged workouts

## Notes

- The original provided Tkinter script was translated into HTTP endpoints so the app can be tested and containerized easily.
- The in-memory workout store resets on each restart; persistence is out of scope for this assignment but can be added later.
- Added conftest.py to resolve the module not found error which was failing the GitHub Work Action.
- This is the Enhancement Branch which is intended to merge into the main branch.
