"""
Web Application using Flask
Provides user interface for the Health & Fitness XAI System
"""
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from main import HealthFitnessXAISystem
from database import UserDatabase
from tracker import DailyTracker
from llm_service import GeminiService
from dotenv import load_dotenv
import secrets
import json
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Security headers
@app.after_request
def set_security_headers(response):
    """Add security headers to all responses"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    return response

# Initialize the system and database
system = HealthFitnessXAISystem()
db = UserDatabase()

# Migrate existing profiles to include calculated metrics
def migrate_profiles():
    """Migrate existing profiles to include BMI, BMR, TDEE calculations"""
    try:
        all_users = db.get_all_users()
        for email, user_data in all_users.items():
            if user_data.get('profile') and user_data['profile'] is not None:
                profile = user_data['profile']
                # Check if profile is missing calculated metrics
                if 'bmi' not in profile or profile.get('bmi') is None:
                    # Recreate the profile with calculations
                    try:
                        from models.user_profile import UserProfile
                        user_profile = UserProfile.from_dict(profile)
                        # Save the updated profile with calculated metrics
                        db.update_user_profile(email, user_profile.to_dict())
                        print(f"✓ Migrated profile for {email}")
                    except Exception as e:
                        print(f"✗ Error migrating profile for {email}: {e}")
    except Exception as e:
        print(f"Migration error: {e}")

# Run migration on startup
migrate_profiles()


@app.route('/')
def index():
    """Home page - redirect to login if not authenticated"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    user_name = session.get('user_name', 'User')
    
    # Check if user has existing profile and should see recommendations
    user_id = session.get('user_id')
    show_recommendations = False
    plan = None
    
    if user_id:
        try:
            # User has profile, generate and show recommendations automatically
            plan = system.generate_complete_plan(user_id)
            
            # Get user profile for Gemini
            user_email = session.get('user_email')
            user_profile = db.get_user_profile(user_email)
            if user_profile:
                try:
                    # Initialize Gemini service
                    gemini = GeminiService()
                    
                    # Create context for Gemini
                    context = f"""
                    Current Plan Summary:
                    - Goal: {plan.get('goal', 'Not specified')}
                    - Daily Calories: {plan.get('daily_calories', 'Not calculated')}
                    - Workout Frequency: {plan.get('workout_frequency', 'Not specified')}
                    - Dietary Focus: {plan.get('dietary_focus', 'Balanced')}
                    """
                    
                    # Get AI-powered advice
                    ai_advice = gemini.get_personalized_advice(
                        user_profile=user_profile,
                        context=context
                    )
                    
                    # Add AI advice to the plan
                    plan['ai_advice'] = ai_advice
                    
                except Exception as e:
                    print(f"Warning: Could not generate AI advice: {e}")
                    plan['ai_advice'] = "AI-powered advice is currently unavailable. Please try again later."
            else:
                plan['ai_advice'] = "Please complete your profile to get personalized AI advice."
            
            show_recommendations = True
        except Exception as e:
            print(f"Error generating plan: {e}")
            # If plan generation fails, show profile form
            show_recommendations = False
    
    return render_template('index.html', user_name=user_name, show_recommendations=show_recommendations, plan=plan)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        # Check for admin credentials
        if email == 'admin@123.com' and password == 'admin123':
            session['user_email'] = email
            session['user_name'] = 'Admin'
            session['is_admin'] = True
            return jsonify({'success': True, 'message': 'Admin login successful', 'is_admin': True})
        
        success, message = db.authenticate_user(email, password)
        
        if success:
            user = db.get_user(email)
            session['user_email'] = email
            session['user_name'] = user['name'] if user else 'User'
            session['is_admin'] = False
            
            # Load existing profile if available
            profile = db.get_user_profile(email)
            has_profile = False
            if profile:
                session['user_id'] = profile['user_id']
                # Recreate user in system
                system.create_user(profile)
                has_profile = True
            
            return jsonify({'success': True, 'message': message, 'is_admin': False, 'has_profile': has_profile})
        else:
            return jsonify({'success': False, 'error': message}), 401
    
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup page"""
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        
        success, message = db.register_user(email, password, name)
        
        if success:
            return jsonify({'success': True, 'message': message})
        else:
            return jsonify({'success': False, 'error': message}), 400
    
    return render_template('signup.html')


@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for('login'))


@app.route('/admin')
def admin_dashboard():
    """Admin dashboard"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    # Check if user is admin
    if not db.is_admin(session['user_email']):
        return "Access Denied: Admin Only", 403
    
    # Get all users
    all_users = db.get_all_users()
    
    return render_template('admin.html', users=all_users)


@app.route('/admin/user/<email>')
def admin_user_detail(email):
    """View specific user details (admin only)"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    if not db.is_admin(session['user_email']):
        return "Access Denied: Admin Only", 403
    
    user = db.get_user(email)
    if not user:
        return "User not found", 404
    
    return render_template('admin_user_detail.html', user_email=email, user=user)


@app.route('/profile')
def user_profile():
    """User profile page"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    # Admins can't access user profile
    if db.is_admin(session['user_email']):
        return redirect(url_for('admin_dashboard'))
    
    user = db.get_user(session['user_email'])
    return render_template('profile.html', user=user, user_email=session['user_email'])


@app.route('/tracker')
def tracker():
    """Daily tracker page"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    return render_template('tracker.html')


@app.route('/dashboard')
def dashboard():
    """Modern dashboard page"""
    if 'user_email' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')


@app.route('/get_user_info', methods=['GET'])
def get_user_info():
    """Get current user information"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    user = db.get_user(session['user_email'])
    if user:
        profile = user.get('profile', {})
        return jsonify({
            'success': True,
            'name': user.get('name', 'User'),
            'email': session['user_email'],
            'sleep_hours': profile.get('sleep_hours', 7.0)
        })
    
    return jsonify({'success': False, 'error': 'User not found'}), 404


@app.route('/create_profile', methods=['POST'])
def create_profile():
    """Create user profile"""
    try:
        data = request.json
        
        # Check if user is logged in
        if 'user_email' not in session:
            return jsonify({
                'success': False,
                'error': 'Please login first'
            }), 401
        
        # Generate unique user ID or use existing
        if 'user_id' in session:
            user_id = session['user_id']
            data['user_id'] = user_id
        else:
            user_id = f"user_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            data['user_id'] = user_id
            session['user_id'] = user_id
        
        # Create user
        user = system.create_user(data)
        
        # Save profile to database (use user.to_dict() to include calculated metrics)
        db.update_user_profile(session['user_email'], user.to_dict())
        
        return jsonify({
            'success': True,
            'user': user.to_dict(),
            'message': 'Profile created successfully!'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/get_recommendations', methods=['GET'])
def get_recommendations():
    """Get personalized recommendations with Gemini AI enhancement"""
    try:
        # Check if user is logged in
        if 'user_email' not in session:
            return jsonify({
                'success': False,
                'error': 'Please login first'
            }), 401
        
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'No user profile found. Please create a profile first.'
            }), 400
        
        # Generate complete plan
        plan = system.generate_complete_plan(user_id)
        
        # Get user profile for Gemini
        user_email = session.get('user_email')
        user_profile = db.get_user_profile(user_email)
        if user_profile:
            try:
                # Initialize Gemini service
                gemini = GeminiService()
                
                # Create context for Gemini
                context = f"""
                Current Plan Summary:
                - Goal: {plan.get('goal', 'Not specified')}
                - Daily Calories: {plan.get('daily_calories', 'Not calculated')}
                - Workout Frequency: {plan.get('workout_frequency', 'Not specified')}
                - Dietary Focus: {plan.get('dietary_focus', 'Balanced')}
                """
                
                # Get AI-powered advice
                ai_advice = gemini.get_personalized_advice(
                    user_profile=user_profile,
                    context=context
                )
                
                # Add AI advice to the plan
                plan['ai_advice'] = ai_advice
                
            except Exception as e:
                print(f"Warning: Could not generate AI advice: {e}")
                plan['ai_advice'] = "AI-powered advice is currently unavailable. Please try again later."
        else:
            plan['ai_advice'] = "Please complete your profile to get personalized AI advice."
        
        return jsonify({
            'success': True,
            'plan': plan
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/update_profile', methods=['POST'])
def update_profile():
    """Update user profile"""
    try:
        if 'user_email' not in session:
            return jsonify({
                'success': False,
                'error': 'Please login first'
            }), 401
        
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'No user profile found.'
            }), 400
        
        updates = request.json
        user = system.update_user(user_id, updates)
        
        # Update in database
        db.update_user_profile(session['user_email'], user.to_dict())
        
        return jsonify({
            'success': True,
            'user': user.to_dict(),
            'message': 'Profile updated successfully!'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/export_plan', methods=['GET'])
def export_plan():
    """Export plan to JSON"""
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'No user profile found.'
            }), 400
        
        plan_json = system.export_plan(user_id)
        
        return jsonify({
            'success': True,
            'plan_json': plan_json
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/tracking_template', methods=['GET'])
def tracking_template():
    """Get progress tracking template"""
    template = system.get_progress_tracking_template()
    return jsonify({
        'success': True,
        'template': template
    })


@app.route('/tracker/today', methods=['GET'])
def get_today_tracker():
    """Get today's tracker data"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    tracker = DailyTracker(session['user_email'])
    today_data = tracker.get_today_data()
    stats = tracker.get_progress_stats()
    
    return jsonify({
        'success': True,
        'data': today_data,
        'stats': stats
    })


@app.route('/tracker/steps', methods=['POST'])
def update_steps():
    """Update step count"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    data = request.json
    steps = data.get('steps', 0)
    
    tracker = DailyTracker(session['user_email'])
    result = tracker.update_steps(steps)
    
    return jsonify({'success': True, 'data': result})


@app.route('/tracker/water', methods=['POST'])
def add_water():
    """Add water intake"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    data = request.json
    ml = data.get('ml', 250)  # Default glass size
    
    tracker = DailyTracker(session['user_email'])
    result = tracker.add_water(ml)
    
    return jsonify({'success': True, 'data': result})


@app.route('/tracker/sleep', methods=['POST'])
def update_sleep():
    """Update sleep hours"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    data = request.json
    hours = data.get('hours', 0)
    
    tracker = DailyTracker(session['user_email'])
    result = tracker.update_sleep(hours)
    
    return jsonify({'success': True, 'data': result})


@app.route('/tracker/meal/<meal_type>/<action>', methods=['POST'])
def toggle_meal(meal_type, action):
    """Mark meal as completed/uncompleted"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    tracker = DailyTracker(session['user_email'])
    
    if action == 'complete':
        result = tracker.complete_meal(meal_type)
    elif action == 'uncomplete':
        result = tracker.uncomplete_meal(meal_type)
    else:
        return jsonify({'success': False, 'error': 'Invalid action'}), 400
    
    return jsonify({'success': True, 'data': result})


@app.route('/tracker/exercise/<day>/<exercise_name>/<action>', methods=['POST'])
def toggle_exercise(day, exercise_name, action):
    """Mark exercise as completed/uncompleted"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    tracker = DailyTracker(session['user_email'])
    
    if action == 'complete':
        result = tracker.complete_exercise(exercise_name, day)
    elif action == 'uncomplete':
        result = tracker.uncomplete_exercise(exercise_name, day)
    else:
        return jsonify({'success': False, 'error': 'Invalid action'}), 400
    
    return jsonify({'success': True, 'data': result})


@app.route('/tracker/replace_food', methods=['POST'])
def replace_food():
    """Replace food item in meal plan"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    data = request.json
    meal_type = data.get('meal_type')
    original_food = data.get('original_food')
    replacement_food = data.get('replacement_food')
    
    tracker = DailyTracker(session['user_email'])
    result = tracker.replace_food(meal_type, original_food, replacement_food)
    
    return jsonify({'success': True, 'data': result})


@app.route('/tracker/weekly', methods=['GET'])
def get_weekly_summary():
    """Get weekly summary"""
    if 'user_email' not in session:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401
    
    tracker = DailyTracker(session['user_email'])
    weekly_data = tracker.get_weekly_summary()
    
    return jsonify({'success': True, 'data': weekly_data})


@app.route('/regenerate-advice', methods=['POST'])
def regenerate_advice():
    """Regenerate AI advice for the current plan"""
    try:
        if 'user_email' not in session:
            return jsonify({
                'success': False,
                'error': 'Please login first'
            }), 401
        
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'No user profile found. Please create a profile first.'
            }), 400
        
        # Generate complete plan
        plan = system.generate_complete_plan(user_id)
        
        # Get user profile for Gemini
        user_email = session.get('user_email')
        user_profile = db.get_user_profile(user_email)
        if user_profile:
            try:
                # Initialize Gemini service
                gemini = GeminiService()
                
                # Create context for Gemini
                context = f"""
                Current Plan Summary:
                - Goal: {plan.get('goal', 'Not specified')}
                - Daily Calories: {plan.get('daily_calories', 'Not calculated')}
                - Workout Frequency: {plan.get('workout_frequency', 'Not specified')}
                - Dietary Focus: {plan.get('dietary_focus', 'Balanced')}
                """
                
                # Get AI-powered advice
                ai_advice = gemini.get_personalized_advice(
                    user_profile=user_profile,
                    context=context
                )
                
                return jsonify({
                    'success': True,
                    'ai_advice': ai_advice
                })
                
            except Exception as e:
                print(f"Warning: Could not generate AI advice: {e}")
                return jsonify({
                    'success': False,
                    'error': 'Failed to generate advice. Please try again.'
                }), 500
        else:
            return jsonify({
                'success': False,
                'error': 'Please complete your profile to get personalized AI advice.'
            }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """Store user feedback on AI advice"""
    try:
        if 'user_email' not in session:
            return jsonify({
                'success': False,
                'error': 'Please login first'
            }), 401
        
        data = request.json
        feedback_type = data.get('type')
        advice_text = data.get('advice_text', '')
        detailed_comment = data.get('detailed_comment')
        
        if not feedback_type:
            return jsonify({
                'success': False,
                'error': 'Feedback type is required'
            }), 400
        
        # Store feedback in database
        db.store_feedback(
            user_email=session['user_email'],
            feedback_type=feedback_type,
            advice_text=advice_text,
            detailed_comment=detailed_comment
        )
        
        return jsonify({
            'success': True,
            'message': 'Feedback submitted successfully'
        })
    
    except Exception as e:
        print(f"Error submitting feedback: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/feedback-stats', methods=['GET'])
def feedback_stats():
    """Get feedback statistics (admin only)"""
    try:
        if 'user_email' not in session:
            return jsonify({
                'success': False,
                'error': 'Please login first'
            }), 401
        
        if not db.is_admin(session['user_email']):
            return jsonify({
                'success': False,
                'error': 'Admin access required'
            }), 403
        
        stats = db.get_feedback_stats()
        
        return jsonify({
            'success': True,
            'stats': stats
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
