from flask import Flask, request, jsonify, render_template
from datetime import datetime

def create_app(test_config: dict | None = None):
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)

    app.workouts = {"Warm-up": [], "Workout": [], "Cool-down": []}

    @app.get("/")
    def index():
        return jsonify(
            message="ACEestFitness API is running", 
            docs=["/health", "/workouts", "/summary", "/workout-chart", "/diet-chart", "/progress"]
        ), 200

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    @app.post("/workouts")
    def add_workout():
        if not request.is_json:
            return jsonify(error="Expected application/json"), 415

        data = request.get_json(silent=True) or {}
        category = data.get("category", "Workout")
        workout = (data.get("workout") or "").strip()
        duration = data.get("duration")

        if category not in app.workouts:
            return jsonify(error="Invalid category. Must be: Warm-up, Workout, or Cool-down"), 400

        if not workout:
            return jsonify(error="Field 'workout' is required"), 400

        try:
            duration = int(duration)
            if duration <= 0:
                raise ValueError
        except Exception:
            return jsonify(error="Field 'duration' must be a positive integer (minutes)"), 400

        entry = {
            "exercise": workout,
            "duration": duration,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        app.workouts[category].append(entry)
        return jsonify(message="Workout added", entry=entry, category=category), 201

    @app.get("/workouts")
    def list_workouts():
        all_workouts = []
        for category, sessions in app.workouts.items():
            for session in sessions:
                all_workouts.append({**session, "category": category})
        return jsonify(workouts=all_workouts, count=len(all_workouts), by_category=app.workouts), 200

    @app.get("/summary")
    def get_summary():
        total_time = sum(
            session['duration'] 
            for sessions in app.workouts.values() 
            for session in sessions
        )
        
        if total_time < 30:
            motivation = "Good start! Keep moving 💪"
        elif total_time < 60:
            motivation = "Nice effort! You're building consistency 🔥"
        else:
            motivation = "Excellent dedication! Keep up the great work 🏆"
        
        return jsonify(
            by_category=app.workouts,
            total_time=total_time,
            motivation=motivation
        ), 200

    @app.get("/workout-chart")
    def workout_chart():
        """Personalized workout chart recommendations"""
        chart_data = {
            "Warm-up (5-10 min)": ["5 min light cardio (Jog/Cycle) to raise heart rate.", "Jumping Jacks (30 reps) for dynamic mobility.", "Arm Circles (15 Fwd/Bwd) to prepare shoulders."],
            "Strength & Cardio (45-60 min)": ["Push-ups (3 sets of 10-15) - Upper body strength.", "Squats (3 sets of 15-20) - Lower body foundation.", "Plank (3 sets of 60 seconds) - Core stabilization.", "Lunges (3 sets of 10/leg) - Balance and leg development."],
            "Cool-down (5 min)": ["Slow Walking - Bring heart rate down gradually.", "Static Stretching (Hold 30s each) - Focus on major muscle groups.", "Deep Breathing Exercises - Aid recovery and relaxation."]
        }
        return jsonify(workout_chart=chart_data), 200

    @app.get("/diet-chart")
    def diet_chart():
        """Best diet chart for fitness goals"""
        diet_plans = {
            "Weight Loss Focus (Calorie Deficit)": ["Breakfast: Oatmeal with Berries (High Fiber).", "Lunch: Grilled Chicken/Tofu Salad (Lean Protein).", "Dinner: Vegetable Soup with Lentils (Low Calorie, High Volume)."],
            "Muscle Gain Focus (High Protein)": ["Breakfast: 3 Egg Omelet, Spinach, Whole-wheat Toast (Protein/Carb combo).", "Lunch: Chicken Breast, Quinoa, and Steamed Veggies (Balanced Meal).", "Post-Workout: Protein Shake & Greek Yogurt (Immediate Recovery)."],
            "Endurance Focus (Complex Carbs)": ["Pre-Workout: Banana & Peanut Butter (Quick Energy).", "Lunch: Whole Grain Pasta with Light Sauce (Sustainable Carbs).", "Dinner: Salmon & Avocado Salad (Omega-3s and Healthy Fats)."]
        }
        return jsonify(diet_plans=diet_plans), 200

    @app.get("/progress")
    def progress():
        """Get progress data for visualization"""
        totals = {
            cat: sum(entry['duration'] for entry in sessions) 
            for cat, sessions in app.workouts.items()
        }
        
        total = sum(totals.values())
        percentages = {
            cat: round((val / total * 100), 1) if total > 0 else 0 
            for cat, val in totals.items()
        }
        
        return jsonify(
            totals=totals,
            percentages=percentages,
            total_time=total
        ), 200
        
    @app.get("/ui")
    def ui():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=8000)
