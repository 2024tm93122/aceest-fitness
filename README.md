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
├── ACEest_Fitness-V1.2.py # Tabbed interface (3 tabs)
├── ACEest_Fitness-V1.2.1.py # Advanced version with progress tracker
├── ACEest_Fitness-V1.2.2.py # Improved UI and styling
├── ACEest_Fitness-V1.2.3.py # Modern design with color palette
├── ACEest_Fitness-V1.3.py # Complete version with PDF reports & BMI/BMR
├── Dockerfile
├── requirements.txt
└── README.md
```

## Features

### **Current API (V1.2.1+)**
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

## 3) Git & GitHub (Version Control)
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
- Test all endpoints (workout-chart, diet-chart, progress)

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

| Version | Date | Features | Key Additions |
|---------|------|----------|---------------|
| **V1.0** | Initial | Basic workout logging (Tkinter) | Simple GUI with add/view workouts |
| **V1.1** | Update 1 | Added categories, timestamps, motivation | Workout categories (Warm-up, Workout, Cool-down) |
| **V1.2** | Update 2 | Tabbed interface (3 tabs) | Workout Chart, Diet Chart tabs |
| **V1.2.1** | Update 3 | Progress Tracker with charts | 4th tab with matplotlib visualizations |
| **V1.2.2** | Update 4 | Enhanced UI styling | Modern theme, better UX |
| **V1.2.3** | Update 5 | Professional color palette | Clean design, improved aesthetics |
| **V1.3** | Latest | PDF reports, BMI/BMR tracking | User info, calorie tracking, PDF export |

## Technology Stack

### **Backend**
- **Flask 3.0.3** - Web framework
- **Gunicorn 22.0.0** - WSGI HTTP Server
- **Python 3.11** - Programming language

### **Testing**
- **Pytest 8.3.2** - Testing framework
- **Requests 2.32.3** - HTTP library for testing

### **Visualization**
- **Matplotlib 3.9.0** - Charts and graphs (V1.2.1+)

### **DevOps**
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Git** - Version control

## Project Structure Details

### **Flask Application (`app/app.py`)**
- Factory pattern with `create_app()`
- In-memory storage with categorized workouts
- RESTful API endpoints
- Template rendering for web UI

### **Tests (`tests/`)**
- Unit tests for all API endpoints
- Validation error testing
- Category-based workout testing
- Health check and summary endpoint tests

### **Docker Configuration**
- Based on Python 3.11 slim image
- Includes curl for health checks
- Runs with Gunicorn for production
- Exposes port 8000

### **CI/CD Pipeline**
- Automated testing on every push
- Docker build and smoke testing
- Multi-step workflow validation
- Endpoint health verification

## Assignment Context

This project is part of the **Introduction to DevOps (CSIZG514/SEZG514)** course assignment, demonstrating:

### **Assignment 1 Requirements**
- ✅ Flask web application development
- ✅ Version control with Git/GitHub
- ✅ Unit testing with Pytest
- ✅ Containerization with Docker
- ✅ CI/CD pipeline with GitHub Actions

### **Assignment 2 Requirements** (Planned)
- ⏳ Jenkins CI/CD pipeline setup
- ⏳ SonarQube code quality analysis
- ⏳ Docker Hub registry integration
- ⏳ Kubernetes deployment (Minikube/Cloud)
- ⏳ Advanced deployment strategies:
  - Blue-Green Deployment
  - Canary Release
  - Rolling Update
  - Shadow Deployment
  - A/B Testing

## Development Roadmap

### **Phase 1: Core Application** ✅ Complete
- Basic Flask API
- Unit tests
- Docker containerization
- GitHub Actions CI

### **Phase 2: Enhanced Features** ✅ Complete
- Workout categories
- Diet planning
- Progress tracking
- Web UI with tabs

### **Phase 3: Advanced DevOps** 🚧 In Progress
- Jenkins integration
- SonarQube quality gates
- Kubernetes deployment
- Advanced deployment strategies

### **Phase 4: Production Ready** 📋 Planned
- Database persistence
- User authentication
- Cloud deployment (AWS/Azure/GCP)
- Monitoring and logging

## Notes

- The original Tkinter scripts demonstrate the evolution from desktop to web application
- The in-memory workout store resets on each restart; persistence will be added in future versions
- All Tkinter versions are preserved to show incremental development
- The Flask API provides the same functionality as Tkinter apps but is containerizable and testable
- Current implementation supports all Assignment 1 requirements
- Assignment 2 requirements are planned for the next phase

## Contributing

This is an academic project for the DevOps course. For any questions or suggestions:
- Check the GitHub Issues
- Review the assignment documentation
- Contact the course instructors

## License

This project is created for educational purposes as part of the BITS Pilani DevOps course.

---

**Last Updated:** Version 1.2.1 - Enhanced with workout charts, diet plans, and progress tracking
