# ACEest Fitness & Gym — V1.2.2 Enhanced UI/UX

A comprehensive Flask API with enhanced Tkinter UI featuring improved styling, tab management, and progress tracking for **ACEest Fitness and Gym**.

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
├── Dockerfile
├── requirements.txt
└── README.md
```

## Features (V1.2.2)

### **Core Features**
- ✅ **Workout Logging** - Track exercises with categories (Warm-up, Workout, Cool-down)
- ✅ **Workout Plan** - Personalized exercise recommendations with detailed instructions
- ✅ **Diet Guide** - Goal-based diet plans (Weight Loss, Muscle Gain, Endurance)
- ✅ **Progress Tracker** - Visual progress with bar and pie charts using matplotlib
- ✅ **RESTful API** - Complete API endpoints for all features
- ✅ **Web UI** - Modern interface with real-time updates
- ✅ **Automated Testing** - Comprehensive pytest coverage
- ✅ **CI/CD Pipeline** - GitHub Actions with Docker builds

### **V1.2.2 Enhancements**
- ✅ **Enhanced UI** - Modern "clam" theme with custom button styles
- ✅ **4 Tabs** - Log Workouts, Workout Plan, Diet Guide, Progress Tracker
- ✅ **Auto-refresh Charts** - Tab change event binding for dynamic updates
- ✅ **Scrollable Summary** - Better data presentation with formatted text
- ✅ **Professional Styling** - Improved colors (#f0f0f0 backgrounds), spacing, and visual hierarchy
- ✅ **Custom Button Styles** - Ttk styled buttons with hover effects
- ✅ **Improved Chart Embedding** - Better matplotlib integration with cleanup

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

## Quick Start

### 1) Run Locally (No Docker)

**Prerequisites:** Python 3.11+
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the app on http://localhost:8000
python -m app.app
```

**Try the API:**
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

# Get progress statistics
curl http://localhost:8000/progress
```

**Run unit tests:**
```bash
pytest -v
```

### 2) Run with Docker
```bash
# Build Docker image
docker build -t aceest-fitness:v1.2.2 .

# Run container
docker run -p 8000:8000 aceest-fitness:v1.2.2
```

### 3) Access Web UI

After starting the app, visit:
```bash
# Open in browser
http://localhost:8000/ui
```

The UI provides:
- **Log Workouts Tab** - Add and view workout sessions by category
- **Workout Plan Tab** - Browse recommended exercises with detailed instructions
- **Diet Guide Tab** - Explore diet plans for different fitness goals
- **Progress Tracker Tab** - Visualize your progress with bar and pie charts

## Technology Stack

### **Backend**
- **Flask 3.0.3** - Web framework
- **Gunicorn 22.0.0** - WSGI HTTP Server
- **Python 3.11** - Programming language

### **Testing**
- **Pytest 8.3.2** - Testing framework
- **Requests 2.32.3** - HTTP library for testing

### **Visualization**
- **Matplotlib 3.9.0** - Charts and graphs for progress tracking

### **DevOps**
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Git** - Version control

## Version History

| Version | Features | Description |
|---------|----------|-------------|
| **V1.0** | Basic workout logging | Simple Tkinter GUI with add/view workouts |
| **V1.1** | Categories & timestamps | Workout categories (Warm-up, Workout, Cool-down) |
| **V1.2** | 3-tab interface | Added Workout Chart and Diet Chart tabs |
| **V1.2.1** | Progress Tracker | 4th tab with matplotlib charts (bar & pie) |
| **V1.2.2** | Enhanced UI/UX | Modern theme, custom styles, auto-refresh |

## What's New in V1.2.2

### **UI/UX Improvements**
- **Modern Theme**: Implemented "clam" ttk theme for cleaner appearance
- **Custom Button Styles**: 
  - Green "Add Session" button with hover effects
  - Blue "View Summary" button with active states
- **Improved Layouts**:
  - Light gray backgrounds (#f0f0f0) for better contrast
  - Card-based input containers with raised relief
  - Better spacing and padding throughout

### **Functionality Enhancements**
- **Tab Change Events**: Auto-refresh progress charts when switching tabs
- **Scrollable Summary Window**: 
  - Text widget with scrollbar for better data viewing
  - Color-coded categories (Blue, Green, Yellow)
  - Formatted timestamps and totals
- **Chart Management**: Proper cleanup of matplotlib widgets to prevent memory leaks
- **Validation**: Positive integer validation for duration input

### **Technical Improvements**
- Event binding for dynamic content updates
- Better widget lifecycle management
- Enhanced status messages with emoji feedback
- Improved chart rendering with tight layout

## Development

### **Project Structure**
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

### **Running Tests Locally**
```bash
# Run all tests with verbose output
pytest -v

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

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Runs Tests**:
   - Installs Python 3.11
   - Installs dependencies
   - Executes pytest

2. **Builds Docker Image**:
   - Creates production-ready container
   - Runs smoke tests

3. **Smoke Tests**:
   - Health check endpoint
   - POST workout operation
   - GET workouts list
   - Summary endpoint
   - Workout chart endpoint
   - Diet chart endpoint
   - Progress endpoint
   - Web UI endpoint

## Assignment Context

This project is part of the **Introduction to DevOps (CSIZG514/SEZG514)** course, demonstrating:

- ✅ CI/CD pipeline implementation
- ✅ Containerization with Docker
- ✅ Automated testing with Pytest
- ✅ RESTful API design
- ✅ Version control with Git/GitHub
- ✅ Progressive feature development
- ✅ UI/UX iteration and improvement

## Notes

- The in-memory workout store resets on each restart; persistence can be added with a database
- V1.2.2 focuses on UI/UX polish without adding new core functionality
- All Tkinter versions are preserved to demonstrate incremental development
- The Flask API supports the same features as the Tkinter desktop application
- Matplotlib is required for progress chart visualization

## Troubleshooting

### **Common Issues**

**Tests failing:**
```bash
# Make sure all dependencies are installed
pip install -r requirements.txt

# Run tests with verbose output to see errors
pytest -vv
```

**Docker build fails:**
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t aceest-fitness:v1.2.2 .
```

**Port already in use:**
```bash
# Use different port
docker run -p 8080:8000 aceest-fitness:v1.2.2

# Or kill the process using port 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux
```

## Contributing

This is an academic project. For questions or issues:
- Check the GitHub Issues
- Review the assignment documentation
- Contact course instructors

## License

This project is created for educational purposes as part of the BITS Pilani DevOps course.

---

**Branch:** `aceest-fitness-v1.2.2`  
**Version:** V1.2.2 - Enhanced UI/UX  
**Last Updated:** November 2024  
**Python Version:** 3.11+  
**Flask Version:** 3.0.3
