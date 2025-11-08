# ACEest Fitness & Gym — V1.2.1

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
├── ACEest_Fitness-V1.2.py # Tabbed interface with 3 tabs
├── ACEest_Fitness-V1.2.1.py # Advanced version with 4 tabs + charts
├── ACEest_Fitness-V1.2.2.py # Enhanced UI styling and UX improvements
├── ACEest_Fitness-V1.2.3.py # Professional color palette and modern design
├── ACEest_Fitness-V1.3.py # Complete version with PDF reports, BMI/BMR
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
# Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# Install dependencies
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
app/
├── __init__.py          # Package initialization
├── app.py               # Flask application with routes
└── templates/
    └── index.html       # Web UI template

tests/
├── conftest.py          # Test configuration
└── test_app.py          # Unit tests

.github/workflows/
└── CI.yml              # CI/CD pipeline configuration
```

- Install deps and run **pytest**
- Build Docker image and run a **smoke test** (health check + sample API calls)
- Test all new endpoints (workout-chart, diet-chart, progress)

# Run tests with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_app.py -v
```

### **Docker Development**
```bash
# Build image
docker build -t aceest-fitness:dev .

# Run with volume mounting for development
docker run -p 8000:8000 -v $(pwd):/app aceest-fitness:dev

# View logs
docker logs <container_id>
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
| **V1.2.2** | Enhanced UI styling & UX | Improved theme, custom button styles, better visual design |
| **V1.2.3** | Professional color palette | Modern design with consistent color scheme and Inter font |
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
- **Enhancements:**
  - Auto-refresh charts when data changes
  - Visual feedback with color-coded categories
  - Professional chart styling

### **V1.2.2 - Enhanced UI & UX**
- **Improvements over V1.2.1:**
  - Implemented "clam" theme for modern look
  - Custom Ttk button styling with active states
  - Tab change event binding for auto-refresh
  - Scrollable summary window with text formatting
  - Enhanced color scheme (#f0f0f0 backgrounds)
  - Better tab labels ("💡 Workout Plan", "🥗 Diet Guide")
  - Improved chart container with proper cleanup
  - More descriptive status messages and feedback
- **Focus Areas:**
  - Visual hierarchy and spacing improvements
  - Better user feedback mechanisms
  - Professional appearance
  - Enhanced readability in all views
- **Technical Changes:**
  - Added `on_tab_change()` event handler
  - Custom button style configurations
  - Improved summary window with scrollbar
  - Better chart embedding and cleanup

### **V1.2.3 - Professional Design**
- **Design Enhancements:**
  - Defined color palette constants (PRIMARY, SECONDARY, BACKGROUND)
  - Inter font family for modern typography
  - Consistent spacing and padding throughout
  - Card-based layout with subtle shadows
  - Better visual hierarchy with color usage
- **Key Features:**
  - Clean, minimalist design philosophy
  - Improved button styling with hover states
  - Enhanced form layouts with better alignment
  - Professional summary views with formatted text
  - Optimized chart colors for accessibility

### **V1.3 - Complete Health Tracking**
- **Major Additions:**
  - User information section (Name, Regn-ID, Age, Gender, Height, Weight)
  - BMI (Body Mass Index) calculation
  - BMR (Basal Metabolic Rate) calculation
  - Calorie tracking using MET values
  - PDF report generation with ReportLab
  - Weekly workout summaries
  - Daily workout tracking
- **Health Metrics:**
  - Automatic BMI calculation from height/weight
  - Gender-specific BMR formulas
  - Exercise-specific calorie burn estimates
- **PDF Features:**
  - Comprehensive weekly fitness reports
  - User health information summary
  - Detailed workout logs with calories
  - Professional table formatting

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

## Development Progression

The project demonstrates incremental development across 8 versions:

1. **V1.0**: Foundation - Basic CRUD operations
2. **V1.1**: Structure - Added categories and timestamps
3. **V1.2**: Organization - Tabbed interface (3 tabs)
4. **V1.2.1**: Visualization - Progress tracking with charts
5. **V1.2.2**: Polish - UI/UX enhancements
6. **V1.2.3**: Design - Professional styling
7. **V1.3**: Completion - Health metrics and PDF reports

Each version builds upon the previous, showcasing:
- Iterative development practices
- Feature expansion
- UI/UX improvements
- Professional maturity

## Notes

- The original provided Tkinter script was translated into HTTP endpoints so the app can be tested and containerized easily.
- The in-memory workout store resets on each restart; persistence is out of scope for this assignment but can be added later.
- Added conftest.py to resolve the module not found error which was failing the GitHub Work Action.
- V1.2 introduces tabbed interface with workout and diet recommendations (3 tabs).
- V1.2.1 extends V1.2 by adding visual progress tracking (4 tabs with matplotlib charts).
- V1.2.2 focuses on UI/UX polish without adding new functionality.
- V1.2.3 implements a professional design system with consistent styling.
- V1.3 adds comprehensive health tracking and reporting capabilities.
- All Tkinter versions are preserved to demonstrate incremental feature development.

## Assignment Context

This project is part of the **Introduction to DevOps (CSIZG514/SEZG514)** course assignment, demonstrating:

### **Assignment 1 & 2 Requirements**
- ✅ Flask web application development
- ✅ Version control with Git/GitHub
- ✅ Unit testing with Pytest
- ✅ Containerization with Docker
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Progressive feature development
- ✅ RESTful API design
- ✅ Automated testing and quality assurance

### **Future Enhancements (Assignment 2 Phase 2)**
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

## Contributing

This is an academic project for the DevOps course. For any questions or suggestions:
- Check the GitHub Issues
- Review the assignment documentation
- Contact the course instructors

## License

This project is created for educational purposes as part of the BITS Pilani DevOps course.

---
