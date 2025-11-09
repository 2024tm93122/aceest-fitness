# 🏋️‍♂️ ACEest Fitness & Gym

A comprehensive **Flask-based fitness management API** that enables workout logging, diet planning, and progress tracking for ACEest Fitness & Gym.  
The project includes RESTful endpoints, Docker support, automated testing, and CI/CD integration with GitHub Actions.

---

## 🚀 Features

✅ **Workout Logging** – Track exercises by category (Warm-up, Workout, Cool-down)  
✅ **Workout Chart** – Personalized exercise recommendations  
✅ **Diet Chart** – Goal-based diet plans (Weight Loss, Muscle Gain, Endurance)  
✅ **Progress Tracker** – Visualize fitness progress using charts  
✅ **RESTful API** – Full CRUD support for workouts, diets, and progress tracking  
✅ **Web UI** – Modern tabbed HTML interface with live updates  
✅ **Automated Testing** – Comprehensive unit tests using Pytest  
✅ **Dockerized Deployment** – Ready for local and production builds  
✅ **CI/CD** – GitHub Actions pipeline for testing and Docker builds  
✅ **SonarQube Ready** – Quality analysis integrated via `sonar-project.properties`

---

## 🧱 Project Structure

aceest-fitness/
├── app/
│ ├── init.py
│ ├── app.py # Flask app factory
│ └── templates/
│ └── index.html # Web interface
├── tests/
│ ├── conftest.py # Pytest configuration
│ └── test_app.py # Unit tests
├── .github/workflows/
│ └── CI.yml # CI/CD pipeline
├── Dockerfile
├── requirements.txt
├── sonar-project.properties
└── README.md


---

## ⚙️ Run Locally

**Prerequisites:**  
- Python 3.11+  
- pip / venv

### 1️⃣ Setup
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

2️⃣ Run the App
python -m app.app

🧪 API Endpoints
| Endpoint         | Method | Description               |
| ---------------- | ------ | ------------------------- |
| `/`              | GET    | API documentation         |
| `/health`        | GET    | Health check              |
| `/workouts`      | POST   | Add a new workout         |
| `/workouts`      | GET    | List all workouts         |
| `/summary`       | GET    | Get workout summary       |
| `/workout-chart` | GET    | Get recommended workouts  |
| `/diet-chart`    | GET    | Get goal-based diet plans |
| `/progress`      | GET    | Get progress statistics   |
| `/ui`            | GET    | Access the web interface  |

🧰 Testing
Run tests:
pytest -v
Generate coverage:
pytest --cov=app tests/
🐳 Run with Docker
docker build -t aceest-fitness:latest .
docker run -p 8000:8000 aceest-fitness:latest
Access the app at:
➡️ http://localhost:8000/ui

⚙️ CI/CD Pipeline

GitHub Actions workflow performs:

Dependency installation

Unit testing with Pytest

Docker image build

Optional push to DockerHub

You can find the workflow at:
.github/workflows/CI.yml

📊 SonarQube Integration

This repo includes sonar-project.properties for SonarQube/SonarCloud analysis.

Configured features:

Code quality scanning

Test coverage reporting

Quality gate enforcement

Ensure your Jenkins or GitHub workflow runs the Sonar scanner after tests.
