# ACEest Fitness & Gym — Introduction To DevOps Assignment 1 Solution

# A minimal Flask API that models basic workout logging for **ACEest_Fitness and Gym**, packaged with unit tests, Dockerfile, and a GitHub Actions CI pipeline.

## Project layout

```text
.
├── app/
│   ├── __init__.py
│   └── app.py            # Flask app (app factory: create_app())
├── tests/
│   └── test_app.py       # Pytest unit tests
├── .github/workflows/
│   └── ci.yml            # GitHub Actions pipeline
├── Dockerfile
├── requirements.txt
└── README.md
```

## 1) Run locally (no Docker)

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

## 3) Git & GitHub (suggested workflow)

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

## Notes

- The original provided Tkinter script was translated into HTTP endpoints so the app can be tested and containerized easily.
- The in-memory workout store resets on each restart; persistence is out of scope for this assignment but can be added later.
- Added conftest.py to resolve the module not found error which was failing the GitHub Work Action.
