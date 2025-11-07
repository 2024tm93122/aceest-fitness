# ACEest Fitness & Gym — Introduction To DevOps Assignment 2 Solution

A comprehensive Flask API that models workout logging, diet planning, and progress tracking for **ACEest Fitness and Gym**, packaged with unit tests, Dockerfile, and a GitHub Actions CI pipeline.

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
├── ACEest_Fitness.py     # Original Tkinter app (V1.0)
├── ACEest_Fitness-V1.1.py # Enhanced version with categories
├── ACEest_Fitness-V1.2.py # Tabbed interface with 3 tabs (Workout Chart, Diet Chart)
├── ACEest_Fitness-V1.2.1.py # Advanced version with 4 tabs (adds Progress Tracker)
├── ACEest_Fitness-V1.2.2.py # Improved UI styling and enhanced user experience
├── ACEest_Fitness-V1.2.3.py # Professional color palette and modern design
├── ACEest_Fitness-V1.3.py # Complete version with PDF reports, BMI/BMR tracking
├── Dockerfile
├── requirements.txt
└── README.md
```

## Features (V1.2.1+)

- ✅ **Workout Logging** - Track exercises with categories (Warm-up, Workout, Cool-down)
- ✅ **Workout Chart** - Personalized exercise recommendations
- ✅ **Diet Chart** - Goal-based diet plans (Weight Loss, Muscle Gain, Endurance)
- ✅ **Progress Tracker** - Visual progress with charts and statistics
- ✅ **RESTful API** - Complete API endpoints for all features
- ✅ **Web UI** - Modern tabbed interface with real-time updates
- ✅ **Automated Testing** - Comprehensive pytest coverage
- ✅ **CI/CD Pipeline** - GitHub Actions with Docker builds

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API documentation |
| `/health` | GET | Health check |
| `/workouts` | POST | Add new workout session |
| `/workouts` | GET | List all workouts |
| `/summary` | GET | Get workout summary with motivation |
| `/workout-chart` | GET | Get workout recommendations |
| `/diet-chart` | GET | Get diet plans by goal |
| `/progress` | GET | Get progress statistics |
| `/ui` | GET | Web interface |

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
# Health check
curl http://localhost:8000/health

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
pytest -v
```

## 2) Run with Docker
```bash
docker build -t aceest-fitness:v1.2.1 .
docker run -p 8000:8000 aceest-fitness:v1.2.1
```

## 3) Git & GitHub (Suggested Workflow)
```bash
git init
git add .
git commit -m "feat: V1.2.1 - Add workout charts, diet plans, and progress tracking"
git tag v1.2.1
git branch -M main
git remote add origin https://github.com/2024tm93122/aceest-fitness.git
git push -u origin main
git push origin v1.2.1
```

Pushes to GitHub will trigger the **CI workflow**:

- Install deps and run **pytest**
- Build Docker image and run a **smoke test** (health check + sample API calls)
- Test all new endpoints (workout-chart, diet-chart, progress)

## 4) Web UI

After starting the app, visit the web interface:
```bash
# Open in browser
http://localhost:8000/ui
```

The UI provides:
- **Log Workouts Tab** - Add and view workout sessions by category
- **Workout Chart Tab** - Browse recommended exercises
- **Diet Chart Tab** - Explore diet plans for different fitness goals
- **Progress Tracker Tab** - Visualize your progress with statistics and charts

## Version History

| Version | Features | Description |
|---------|----------|-------------|
| **V1.0** | Basic workout logging (Tkinter) | Simple desktop GUI with add/view workouts functionality |
| **V1.1** | Added categories, timestamps, motivation | Workout categories (Warm-up, Workout, Cool-down) with time tracking |
| **V1.2** | Tabbed interface with 3 tabs | Added Workout Chart and Diet Chart tabs (no progress tracker) |
| **V1.2.1** | Added 4th tab: Progress Tracker | Complete tabbed UI with visual charts using matplotlib |
| **V1.2.2** | Enhanced UI styling | Improved theme, better UX, modern styling |
| **V1.2.3** | Professional color palette | Clean design with consistent color scheme |
| **V1.3** | PDF reports & health metrics | User info, BMI/BMR calculation, calorie tracking, PDF export |

## Version Details

### **V1.2 - Tabbed Interface Introduction**
- **Added Features:**
  - Tabbed notebook interface using ttk.Notebook
  - Workout Chart tab with exercise recommendations
  - Diet Chart tab with goal-based meal plans
  - Three main tabs: Log Workouts, Workout Chart, Diet Chart
- **Key Differences from V1.1:**
  - Moved from single window to multi-tab interface
  - Added static workout and diet recommendations
  - Improved organization and user navigation
- **Note:** V1.2 does NOT include the Progress Tracker tab (that's V1.2.1+)

### **V1.2.1 - Progress Visualization**
- **Added Features:**
  - 4th tab: Progress Tracker with matplotlib charts
  - Bar chart showing time spent per category
  - Pie chart showing workout distribution
  - Dynamic chart updates after adding workouts
- **Dependencies:** Requires matplotlib for chart rendering

## Notes

- The original provided Tkinter script was translated into HTTP endpoints so the app can be tested and containerized easily.
- The in-memory workout store resets on each restart; persistence is out of scope for this assignment but can be added later.
- Added conftest.py to resolve the module not found error which was failing the GitHub Work Action.
- V1.2 introduces tabbed interface with workout and diet recommendations (3 tabs).
- V1.2.1 extends V1.2 by adding visual progress tracking (4 tabs with matplotlib charts).
- All Tkinter versions are preserved to demonstrate incremental feature development.

## Assignment Context

This project is part of the **Introduction to DevOps (CSIZG514/SEZG514)** course assignment, demonstrating:
- CI/CD pipeline implementation
- Containerization with Docker
- Automated testing with Pytest
- RESTful API design
- Version control with Git/GitHub
- Progressive feature development across multiple versions
