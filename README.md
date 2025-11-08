# ACEest Fitness & Gym — V1.2.3 Professional Design

A comprehensive Flask API with professional color palette and modern typography for **ACEest Fitness and Gym**.

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
├── ACEest_Fitness-V1.2.3.py # Professional color palette and Inter font
├── Dockerfile
├── requirements.txt
└── README.md
```

## Features (V1.2.3)

### **Core Features**
- ✅ **Workout Logging** - Track exercises with categories (Warm-up, Workout, Cool-down)
- ✅ **Workout Plan** - Personalized exercise recommendations with detailed instructions
- ✅ **Diet Guide** - Goal-based nutritional plans with calorie focus
- ✅ **Progress Tracker** - Visual progress with professional bar and pie charts
- ✅ **RESTful API** - Complete API endpoints for all features
- ✅ **Web UI** - Modern interface with real-time updates
- ✅ **Automated Testing** - Comprehensive pytest coverage
- ✅ **CI/CD Pipeline** - GitHub Actions with Docker builds

### **V1.2.3 Design Enhancements**
- ✅ **Professional Color Palette** - Consistent design system with defined constants
  - Primary: `#4CAF50` (Vibrant Green)
  - Secondary: `#2196F3` (Bright Blue)
  - Background: `#F8F9FA` (Very Light Gray)
  - Card Background: `#FFFFFF` (White)
  - Text: `#343A40` (Dark Charcoal)
- ✅ **Inter Font Family** - Modern, readable typography throughout
- ✅ **Card-Based Layout** - Clean, organized UI with subtle borders
- ✅ **Improved Visual Hierarchy** - Better use of spacing, padding, and colors
- ✅ **Enhanced Chart Styling** - Professional matplotlib integration
- ✅ **Accessibility** - Better color contrast and readable text

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
docker build -t aceest-fitness:v1.2.3 .

# Run container
docker run -p 8000:8000 aceest-fitness:v1.2.3
```

### 3) Access Web UI

After starting the app, visit:
```bash
# Open in browser
http://localhost:8000/ui
```

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

| Version | Key Features | Design Focus |
|---------|-------------|--------------|
| **V1.0** | Basic workout logging | Simple Tkinter GUI |
| **V1.1** | Categories & timestamps | Data organization |
| **V1.2** | 3-tab interface | UI structure |
| **V1.2.1** | Progress charts | Data visualization |
| **V1.2.2** | Enhanced styling | Modern theme |
| **V1.2.3** | Professional design | Color system & typography |

## What's New in V1.2.3

### **Design System**
- **Defined Color Constants**: All colors defined as constants for consistency
  - `COLOR_PRIMARY`: #4CAF50 (Success/Add actions)
  - `COLOR_SECONDARY`: #2196F3 (Info/Summary actions)
  - `COLOR_BACKGROUND`: #F8F9FA (Main background)
  - `COLOR_CARD_BG`: #FFFFFF (Card backgrounds)
  - `COLOR_TEXT`: #343A40 (Primary text color)

### **Typography**
- **Inter Font**: Modern, highly readable font family
- **Consistent Font Sizes**: 20px headers, 12px body text, 11px secondary
- **Bold Weights**: Strategic use of bold for emphasis

### **Layout Improvements**
- **Larger Window**: 850x700 for better content display
- **Card-Based Design**: Input forms in raised cards with subtle borders
- **Better Spacing**: Increased padding (padx=20, pady=20)
- **Visual Hierarchy**: Clear distinction between headers, content, and actions

### **Chart Enhancements**
- **Professional Styling**: Charts use the defined color palette
- **Better Contrast**: White backgrounds for charts
- **Cleaner Axes**: Removed unnecessary spines, added subtle gridlines
- **Consistent Colors**: Blue, Green, Yellow for Warm-up, Workout, Cool-down

### **Button Styling**
- **Custom Ttk Styles**: Primary (green) and Secondary (blue) button styles
- **Active States**: Darker colors on hover (#388E3C, #1976D2)
- **Better Padding**: 10px padding for comfortable clicking

### **Summary Window**
- **Professional Header**: "Full Session History" with emoji
- **Scrollbar Styling**: Clean ttk scrollbar
- **Color-Coded Categories**: Blue, Green, Yellow for different workout types
- **Formatted Text**: Bold headers, italic empty states, red totals

## Assignment Context

This project is part of the **Introduction to DevOps (CSIZG514/SEZG514)** course, demonstrating:

- ✅ CI/CD pipeline implementation
- ✅ Containerization with Docker
- ✅ Automated testing with Pytest
- ✅ RESTful API design
- ✅ Version control with Git/GitHub
- ✅ Progressive feature development
- ✅ Professional UI/UX design principles

## Notes

- V1.2.3 focuses on design polish with a professional color system
- The Inter font provides modern, readable typography
- All styling uses defined color constants for consistency
- The Flask API remains unchanged from V1.2.2
- Matplotlib charts use the same color palette as the UI

## License

This project is created for educational purposes as part of the BITS Pilani DevOps course.

---

**Branch:** `aceest-fitness-v1.2.3`  
**Version:** V1.2.3 - Professional Design  
**Last Updated:** November 2024  
**Python Version:** 3.11+  
**Flask Version:** 3.0.3
