# Health & Fitness XAI System

## Overview
An advanced health and fitness recommendation system that uses **Explainable Artificial Intelligence (XAI)** to provide personalized diet and exercise plans with clear, understandable explanations.

## Features

### ✅ Objective 1: User Data Collection & Management
- Comprehensive user profile system collecting:
  - Basic metrics: Age, weight, height, gender
  - Activity level assessment
  - Fitness goals (weight loss, muscle gain, maintenance, endurance)
  - Dietary restrictions and medical conditions
- Automatic calculation of:
  - BMI (Body Mass Index)
  - BMR (Basal Metabolic Rate using Mifflin-St Jeor Equation)
  - TDEE (Total Daily Energy Expenditure)

### ✅ Objective 2: XAI-Based Recommendation System
- **Diet Recommendations:**
  - Personalized calorie targets based on goals
  - Optimized macronutrient distribution (protein, carbs, fats)
  - Sample meal plans with specific food items and quantities
  - Clear explanations for every recommendation

- **Exercise Recommendations:**
  - Customized workout splits (cardio, strength, flexibility)
  - Weekly workout plans with specific exercises
  - Sets, reps, and duration for each exercise
  - Expected calorie burn calculations

### ✅ Objective 3: Clear & Understandable Explanations
- **XAI Techniques Implemented:**
  - Feature importance visualization
  - Decision factor analysis
  - Step-by-step reasoning for recommendations
  - Outcome predictions with confidence levels

- **Transparency Features:**
  - Why each calorie target was chosen
  - How activity level affects recommendations
  - Impact of each user characteristic on the plan
  - Scientific basis for calculations (BMR formulas, etc.)

## System Architecture

```
health_fitness_xai/
├── models/
│   ├── __init__.py
│   └── user_profile.py          # User data model with health metrics
├── engines/
│   ├── __init__.py
│   ├── diet_engine.py           # Diet recommendation engine with XAI
│   └── exercise_engine.py       # Exercise recommendation engine with XAI
├── templates/
│   └── index.html               # Web interface
├── main.py                      # Core system integration
├── app.py                       # Flask web application
└── requirements.txt             # Python dependencies
```

## Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**

**Option A: Command-line interface**
```bash
python main.py
```

**Option B: Web interface**
```bash
python app.py
```
Then open your browser to: http://localhost:5000

## Usage

### Web Interface
1. Open the application in your browser
2. Fill in your personal information:
   - Name, age, gender
   - Weight and height
   - Activity level
   - Fitness goals
   - Dietary restrictions (optional)
3. Click "Generate My Personalized Plan"
4. View your personalized recommendations across 4 tabs:
   - **Overview:** Key metrics and expected outcomes
   - **Diet Plan:** Calorie targets, macros, and meal plans
   - **Exercise Plan:** Weekly workout schedule
   - **Why This Works:** XAI explanations and decision factors

### Command-line Interface
The `main.py` file contains a demonstration that:
- Creates a sample user profile
- Generates complete recommendations
- Displays detailed explanations
- Shows all XAI components

## XAI Components

### 1. Feature Importance
Shows the relative contribution of each user characteristic:
- Fitness goal (40%)
- Activity level (25%)
- BMI (15%)
- Age (10%)
- Current fitness (10%)

### 2. Decision Factors
Explains key factors influencing recommendations:
- **BMI Category:** Impact on calorie recommendations
- **Activity Level:** Effect on TDEE and workout frequency
- **Fitness Goal:** Determines calorie surplus/deficit and exercise split
- **Age:** Influences recovery time and exercise intensity

### 3. Transparent Calculations
All calculations are explained:
- BMR using Mifflin-St Jeor: `10 × weight + 6.25 × height - 5 × age + s`
- TDEE: `BMR × Activity Multiplier`
- Calorie deficit/surplus based on goal
- Macronutrient distribution rationale

### 4. Outcome Predictions
Predicts expected results with:
- Timeframe (4 weeks)
- Expected weight change
- Confidence level
- Scientific explanation

## Key Algorithms

### Diet Recommendation Engine
- **Calorie Calculation:** Based on TDEE with goal-specific adjustments
- **Macro Distribution:** Optimized ratios for each goal type
- **Meal Planning:** Balanced meals from nutrient database
- **Explanation Generation:** Step-by-step reasoning for each recommendation

### Exercise Recommendation Engine
- **Exercise Split:** Goal-based distribution of workout types
- **Progressive Planning:** Gradual intensity increase
- **Calorie Burn Estimation:** Weight-adjusted calculations
- **Recovery Optimization:** Built-in rest days and active recovery

## Scientific Basis

### BMR Calculation (Mifflin-St Jeor Equation)
- **Men:** BMR = 10W + 6.25H - 5A + 5
- **Women:** BMR = 10W + 6.25H - 5A - 161
- W = weight (kg), H = height (cm), A = age (years)

### TDEE Multipliers
- Sedentary: 1.2
- Lightly Active: 1.375
- Moderately Active: 1.55
- Very Active: 1.725
- Extra Active: 1.9

### Calorie-Weight Relationship
- 7700 calories ≈ 1 kg of body fat
- Safe weight loss: 0.5-1 kg/week (500-1000 cal deficit)
- Safe muscle gain: 0.25-0.5 kg/week (300-500 cal surplus)

## Advantages of This System

### 1. Trust Through Transparency
- Users understand WHY recommendations are made
- Scientific basis clearly explained
- No "black box" AI decisions

### 2. Personalization
- Every plan is unique to the individual
- Considers multiple factors simultaneously
- Adapts to different goals and restrictions

### 3. Education
- Users learn about nutrition and fitness
- Empowers informed decision-making
- Promotes long-term lifestyle changes

### 4. Safety
- Recommendations within safe limits
- No extreme diets or workout plans
- Considers age and current fitness level

## Future Enhancements

- Integration with fitness trackers
- Machine learning for plan optimization
- Progress tracking and plan adjustments
- Social features and community support
- Mobile application
- Advanced XAI techniques (SHAP, LIME)
- Meal prep and shopping list generation

## Technical Details

**Backend:** Python with Flask
**Frontend:** HTML, CSS, JavaScript
**Data Models:** Object-oriented design with dataclasses
**XAI Approach:** Feature importance + Decision factors + Transparent calculations

## Example Output

### Sample User Profile
- Age: 30, Male, 85kg, 175cm
- Activity: Moderately Active
- Goal: Weight Loss

### Generated Recommendations
- **Daily Calories:** 2,113 (500 cal deficit from TDEE)
- **Macros:** 158g protein, 211g carbs, 70g fats
- **Weekly Exercise:** 260 min, 1,520 calories burned
- **Expected Loss:** 0.8 kg/week (3.2 kg in 4 weeks)

### XAI Explanations
- "Your BMR is 1,826 calories - this is what your body burns at rest."
- "With your moderately active lifestyle, your TDEE is 2,613 calories."
- "To lose weight safely, we've created a 500 calorie deficit."
- "High cardio proportion (60%) maximizes fat burning."

## License
This project is for educational and demonstration purposes.

## Support
For questions or issues, please refer to the code documentation or create an issue.
