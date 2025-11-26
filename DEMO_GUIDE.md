# Health & Fitness XAI System - Demo Guide

## Quick Start

### Option 1: Command-Line Demo
```bash
cd d:/SiddarthK/health_fitness_xai
python main.py
```

This will run a demonstration with a sample user and display:
- User profile and health metrics
- Complete diet plan with explanations
- Weekly exercise schedule
- XAI explanations showing why each recommendation was made

### Option 2: Web Application
```bash
cd d:/SiddarthK/health_fitness_xai
pip install -r requirements.txt
python app.py
```

Then open your browser to: **http://localhost:5000**

## System Demonstration

### 1. User Profile Creation
The system collects:
- **Basic Info:** Name, age, gender
- **Physical Metrics:** Weight (kg), height (cm)
- **Activity Level:** From sedentary to extra active
- **Goals:** Weight loss, muscle gain, maintenance, endurance
- **Restrictions:** Dietary preferences and medical conditions

### 2. Automated Calculations
The system automatically calculates:
- **BMI:** Body Mass Index with category classification
- **BMR:** Basal Metabolic Rate (Mifflin-St Jeor equation)
- **TDEE:** Total Daily Energy Expenditure

### 3. Personalized Recommendations

#### Diet Plan Includes:
- Daily calorie target adjusted for goals
- Macronutrient distribution (protein, carbs, fats)
- Sample meal plan with specific foods and quantities
- Daily nutritional totals

#### Exercise Plan Includes:
- Exercise type distribution (cardio, strength, flexibility)
- Complete 7-day weekly schedule
- Specific exercises with sets, reps, and duration
- Expected weekly calorie burn

### 4. XAI Explanations

The system provides transparent explanations:

#### A. Calorie Explanations
- "Your BMR is X calories - this is what your body burns at rest"
- "With your activity level, your TDEE is Y calories"
- "To achieve your goal, we've created a Z calorie deficit/surplus"

#### B. Macro Explanations
- Why protein percentage is set for your goal
- How carbs support your activity level
- Why fats are important for hormones

#### C. Feature Importance
Shows percentage contribution of each factor:
- Fitness Goal: 40%
- Activity Level: 25%
- BMI: 15%
- Age: 10%
- Current Fitness: 10%

#### D. Decision Factors
For each major factor, explains:
- Current value
- Impact level (Low/Medium/High/Very High)
- Specific explanation of how it affects recommendations

### 5. Outcome Predictions
The system predicts:
- Expected weight change in 4 weeks
- Confidence level (based on adherence factors)
- Scientific reasoning behind predictions

## Example Test Cases

### Test Case 1: Weight Loss
```python
user_data = {
    'name': 'John Doe',
    'age': 30,
    'gender': 'male',
    'weight': 85,
    'height': 175,
    'activity_level': 'moderately_active',
    'fitness_goals': ['weight_loss']
}
```

**Expected Results:**
- BMI: 27.76 (Overweight)
- TDEE: ~2788 calories
- Target: ~2288 calories (500 deficit)
- Exercise: 60% cardio, 30% strength, 10% flexibility
- Expected loss: 0.7 kg/week

### Test Case 2: Muscle Gain
```python
user_data = {
    'name': 'Jane Smith',
    'age': 25,
    'gender': 'female',
    'weight': 60,
    'height': 165,
    'activity_level': 'very_active',
    'fitness_goals': ['muscle_gain']
}
```

**Expected Results:**
- BMI: 22.04 (Normal)
- TDEE: ~2156 calories
- Target: ~2456 calories (300 surplus)
- Exercise: 70% strength, 20% cardio, 10% flexibility
- Macros: 35% protein, 45% carbs, 20% fats

### Test Case 3: Endurance
```python
user_data = {
    'name': 'Mike Runner',
    'age': 35,
    'gender': 'male',
    'weight': 70,
    'height': 178,
    'activity_level': 'extra_active',
    'fitness_goals': ['endurance']
}
```

**Expected Results:**
- Exercise: 70% cardio, 20% strength, 10% flexibility
- Macros: Higher carbs (55%) for energy
- Focus on stamina-building exercises

## XAI Features Demonstrated

### 1. Transparency
Every recommendation includes:
- The calculation method
- The reasoning behind choices
- Scientific basis (formulas, research)

### 2. Interpretability
Non-technical users can understand:
- Why they received specific recommendations
- How changing factors would affect the plan
- What each metric means for their health

### 3. Trust Building
Users see:
- Feature importance rankings
- Decision factor analysis
- Confidence levels for predictions
- Limitations and disclaimers

### 4. Educational Value
The system teaches users about:
- BMR and TDEE concepts
- Macronutrient roles
- Exercise types and benefits
- Sustainable health practices

## Verification Points

To verify the system meets objectives:

**✓ Objective 1: Data Collection**
- [x] Collects age, weight, height, activity level
- [x] Stores and manages user information
- [x] Calculates derived metrics (BMI, BMR, TDEE)

**✓ Objective 2: XAI Recommendations**
- [x] Generates personalized diet plans
- [x] Generates personalized exercise plans
- [x] Uses XAI techniques for explanations
- [x] Adapts to user goals and restrictions

**✓ Objective 3: Clear Explanations**
- [x] Provides step-by-step reasoning
- [x] Shows feature importance
- [x] Explains decision factors
- [x] Uses non-technical language
- [x] Includes scientific basis

## Interactive Web Demo Features

### User Interface Highlights:
1. **Profile Form:** Easy-to-use inputs with validation
2. **Tabbed Results:** Organized information display
3. **Visual Metrics:** Large, easy-to-read key numbers
4. **Color-Coded Impact:** Visual importance indicators
5. **Progress Bars:** Feature importance visualization
6. **Responsive Design:** Works on all screen sizes

### Navigation:
- **Overview Tab:** Summary and key metrics
- **Diet Plan Tab:** Calorie targets, macros, meals
- **Exercise Plan Tab:** Weekly workout schedule
- **Why This Works Tab:** Complete XAI explanations

## Troubleshooting

### Common Issues:

**Issue:** Module not found error
**Solution:** Install requirements: `pip install -r requirements.txt`

**Issue:** Port already in use
**Solution:** Change port in app.py: `app.run(port=5001)`

**Issue:** No recommendations shown
**Solution:** Check that at least one fitness goal is selected

## Additional Features

### Export Functionality
Export your complete plan as JSON for:
- Sharing with healthcare providers
- Importing into other apps
- Keeping personal records

### Progress Tracking Template
Get a template for tracking:
- Weekly weight measurements
- Body measurements
- Energy levels
- Workout completion
- Diet adherence

## Conclusion

This system demonstrates a complete health and fitness recommendation platform with:
- Comprehensive user profiling
- Science-based calculations
- Personalized recommendations
- Transparent XAI explanations
- Professional web interface

All objectives have been successfully achieved with clear, understandable explanations that build user trust and engagement.
