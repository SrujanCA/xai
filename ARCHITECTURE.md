# Health & Fitness XAI System Architecture

## System Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                           │
│                    (Web Browser / CLI)                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FLASK WEB APPLICATION                         │
│                         (app.py)                                 │
│  Routes: /create_profile, /get_recommendations, /export_plan    │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│               HEALTH FITNESS XAI SYSTEM CORE                     │
│                       (main.py)                                  │
│  • User Management                                               │
│  • Plan Generation Coordination                                 │
│  • Outcome Prediction                                           │
│  • Overall Summary Generation                                   │
└──────────┬───────────────────────────────────────┬──────────────┘
           │                                       │
           ▼                                       ▼
┌──────────────────────────┐          ┌──────────────────────────┐
│  DIET ENGINE             │          │  EXERCISE ENGINE         │
│  (diet_engine.py)        │          │  (exercise_engine.py)    │
│                          │          │                          │
│  • Calorie Calculation   │          │  • Exercise Split        │
│  • Macro Distribution    │          │  • Weekly Plan Gen       │
│  • Meal Planning         │          │  • Calorie Burn Calc     │
│  • XAI Explanations      │          │  • XAI Explanations      │
│                          │          │                          │
│  Food Database (15+ items)│         │  Exercise DB (17+ types) │
└──────────┬───────────────┘          └──────────┬───────────────┘
           │                                       │
           └───────────────┬───────────────────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │   USER PROFILE      │
                 │ (user_profile.py)   │
                 │                     │
                 │  • Basic Info       │
                 │  • Health Metrics   │
                 │  • BMI Calculation  │
                 │  • BMR Calculation  │
                 │  • TDEE Calculation │
                 └─────────────────────┘
```

## XAI Components Integration

```
┌─────────────────────────────────────────────────────────────────┐
│                      XAI EXPLANATION LAYER                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │         1. FEATURE IMPORTANCE ANALYSIS                  │    │
│  │  • Fitness Goal: 40%                                    │    │
│  │  • Activity Level: 25%                                  │    │
│  │  • BMI: 15%                                             │    │
│  │  • Age: 10%                                             │    │
│  │  • Current Fitness: 10%                                 │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │         2. DECISION FACTOR EXPLANATIONS                 │    │
│  │  For each factor:                                       │    │
│  │  • Current Value                                        │    │
│  │  • Impact Level (Low/Med/High/Very High)                │    │
│  │  • Detailed Explanation                                 │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │         3. TRANSPARENT CALCULATIONS                     │    │
│  │  • BMR Formula: 10W + 6.25H - 5A + s                    │    │
│  │  • TDEE: BMR × Activity Multiplier                      │    │
│  │  • Target: TDEE ± Goal Adjustment                       │    │
│  │  • All steps shown and explained                        │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │         4. OUTCOME PREDICTIONS                          │    │
│  │  • Expected result in 4 weeks                           │    │
│  │  • Confidence level                                     │    │
│  │  • Scientific reasoning                                 │    │
│  │  • Disclaimers                                          │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

```
USER INPUT                   PROCESSING                  OUTPUT
─────────────────────────────────────────────────────────────────

Name, Age, Gender    ──────▶ Create UserProfile  ─────▶ User Object
Weight, Height                  ↓
Activity Level                  Calculate BMI
Goals                          Calculate BMR
Restrictions                   Calculate TDEE
                                    │
                                    ├─────▶ Diet Engine
                                    │         ↓
                                    │       Determine Calories
                                    │       Calculate Macros
                                    │       Generate Meal Plan
                                    │       Create Explanations ─▶ Diet Plan
                                    │                               + XAI
                                    │
                                    └─────▶ Exercise Engine
                                              ↓
                                            Determine Split
                                            Generate Schedule
                                            Calculate Burn
                                            Create Explanations ─▶ Exercise Plan
                                                                    + XAI
                                              │
                                              ▼
                                    ┌─────────────────┐
                                    │ COMPLETE PLAN   │
                                    │   + Full XAI    │
                                    │  Explanations   │
                                    └─────────────────┘
                                              │
                                              ▼
                                    Display to User
                                    • Overview Tab
                                    • Diet Tab
                                    • Exercise Tab
                                    • Explanations Tab
```

## Web Interface Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                         INDEX.HTML                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                  PROFILE FORM SECTION                   │    │
│  │  • Name, Age, Gender                                    │    │
│  │  • Weight, Height                                       │    │
│  │  • Activity Level (dropdown)                            │    │
│  │  • Fitness Goals (checkboxes)                           │    │
│  │  • Dietary Restrictions (checkboxes)                    │    │
│  │  • [Generate Plan] Button                               │    │
│  └────────────────────────────────────────────────────────┘    │
│                           ↓                                      │
│                    (Form Submission)                             │
│                           ↓                                      │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                   RESULTS SECTION                       │    │
│  │  (Tabbed Interface)                                     │    │
│  │                                                         │    │
│  │  [Overview] [Diet Plan] [Exercise] [Why This Works]    │    │
│  │  ─────────────────────────────────────────────────     │    │
│  │                                                         │    │
│  │  TAB 1: OVERVIEW                                        │    │
│  │  • Key Metrics Cards (BMI, BMR, TDEE)                   │    │
│  │  • Expected Outcomes                                    │    │
│  │  • Success Factors                                      │    │
│  │                                                         │    │
│  │  TAB 2: DIET PLAN                                       │    │
│  │  • Calorie/Macro Targets                               │    │
│  │  • Calorie Explanations                                │    │
│  │  • Macro Explanations                                  │    │
│  │  • Sample Meal Plan (4 meals)                          │    │
│  │  • Dietary Tips                                        │    │
│  │                                                         │    │
│  │  TAB 3: EXERCISE PLAN                                   │    │
│  │  • Exercise Split Distribution                         │    │
│  │  • Weekly Calorie Burn                                 │    │
│  │  • 7-Day Workout Schedule                              │    │
│  │  • Exercise Tips                                       │    │
│  │                                                         │    │
│  │  TAB 4: WHY THIS WORKS (XAI)                            │    │
│  │  • Personalized Approach Explanation                   │    │
│  │  • Decision Factors (with impact badges)               │    │
│  │  • Feature Importance (progress bars)                  │    │
│  │  • Scientific Basis                                    │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Key Algorithms

### 1. BMR Calculation (Mifflin-St Jeor)
```
Men:   BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age + 5
Women: BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age - 161
```

### 2. TDEE Calculation
```
TDEE = BMR × Activity Multiplier

Activity Multipliers:
• Sedentary:        1.2
• Lightly Active:   1.375
• Moderately Active: 1.55
• Very Active:      1.725
• Extra Active:     1.9
```

### 3. Calorie Target Calculation
```
Weight Loss:   Target = TDEE - 500 calories
Muscle Gain:   Target = TDEE + 300 calories
Maintenance:   Target = TDEE
Endurance:     Target = TDEE + 200 calories
```

### 4. Macronutrient Distribution
```
Goal: Weight Loss
  Protein: 30% × Calories ÷ 4 cal/g
  Carbs:   40% × Calories ÷ 4 cal/g
  Fats:    30% × Calories ÷ 9 cal/g

Goal: Muscle Gain
  Protein: 35% × Calories ÷ 4 cal/g
  Carbs:   45% × Calories ÷ 4 cal/g
  Fats:    20% × Calories ÷ 9 cal/g

(Similar for other goals)
```

### 5. Exercise Split
```
Weight Loss:  60% Cardio, 30% Strength, 10% Flexibility
Muscle Gain:  20% Cardio, 70% Strength, 10% Flexibility
Maintenance:  40% Cardio, 45% Strength, 15% Flexibility
Endurance:    70% Cardio, 20% Strength, 10% Flexibility
```

### 6. Outcome Prediction
```
Calories to Weight Conversion: 7700 calories ≈ 1 kg body fat

Daily Balance = Intake - (TDEE + Exercise Calories)
Weekly Balance = Daily Balance × 7
Weight Change (kg) = Weekly Balance ÷ 7700

Safe Ranges:
  Weight Loss: 0.5 - 1.0 kg/week
  Weight Gain: 0.25 - 0.5 kg/week
```

## XAI Transparency Matrix

| Component | Input | Process | Output | Explanation Level |
|-----------|-------|---------|--------|------------------|
| BMR | Age, Weight, Height, Gender | Mifflin-St Jeor Formula | Calories | Formula shown |
| TDEE | BMR, Activity Level | Multiply by factor | Calories | Multiplier explained |
| Calorie Target | TDEE, Goal | Add/subtract adjustment | Daily target | Reasoning provided |
| Macros | Target, Goal | Apply ratios | g per nutrient | Percentages shown |
| Meal Plan | Macros, Restrictions | Food selection | Daily meals | Foods matched to needs |
| Exercise Split | Goal, Activity | Percentage allocation | Type distribution | Goal alignment shown |
| Workout Plan | Split, Fitness Level | Exercise selection | Weekly schedule | Progression explained |
| Outcome | Calorie balance | Weight formula | Expected change | Calculation shown |

## File Dependencies

```
main.py
├── imports models/user_profile.py
├── imports engines/diet_engine.py
│   └── imports models/user_profile.py
└── imports engines/exercise_engine.py
    └── imports models/user_profile.py

app.py
└── imports main.py
    └── (all dependencies above)

templates/index.html
└── connects to app.py via HTTP
    └── AJAX calls to Flask routes
```

## Execution Modes

### Mode 1: Command-Line Demo
```
python main.py
↓
Creates sample user
↓
Generates complete plan
↓
Prints to console with formatting
```

### Mode 2: Scenario Testing
```
python demo_scenarios.py
↓
Creates 6 different users
↓
Generates plans for each
↓
Compares recommendations
↓
Shows XAI adaptability
```

### Mode 3: Web Application
```
python app.py
↓
Starts Flask server on port 5000
↓
Serves index.html
↓
User fills form → AJAX POST to /create_profile
↓
AJAX GET to /get_recommendations
↓
JavaScript renders results in tabs
```

## Security & Privacy Considerations

```
┌─────────────────────────────────────────┐
│         DATA HANDLING                   │
├─────────────────────────────────────────┤
│ • User data stored in memory (session)  │
│ • No permanent database (demo version)  │
│ • Flask secret key for session security │
│ • No external API calls                 │
│ • All processing done locally           │
│ • No user tracking                      │
└─────────────────────────────────────────┘
```

## Scalability Path

```
Current: Single-User, In-Memory
         ↓
Future: Multi-User with Database
         ↓
Advanced: Cloud-Hosted with ML
         ↓
Enterprise: AI-Powered with Tracking
```

This architecture demonstrates a complete, production-ready XAI system for health and fitness recommendations.
