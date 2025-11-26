"""
LLM Service for Health & Fitness XAI System
Uses Google's Gemini API for enhanced recommendations
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from typing import Dict, Optional

load_dotenv()

class GeminiService:
    def __init__(self):
        """Initialize the Gemini service with API key"""
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key or api_key == 'your_api_key_here':
            raise ValueError(
                "Please set your GOOGLE_API_KEY in the .env file. "
                "Get it from: https://makersuite.google.com/"
            )
        
        genai.configure(api_key=api_key)
        # Using the latest stable model
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
    def get_personalized_advice(self, user_profile: Dict, context: str) -> str:
        """
        Get personalized health/fitness advice using Google Gemini
        
        Args:
            user_profile: Dictionary containing user details
            context: Current plan context/summary
            
        Returns:
            str: Personalized advice or error message
        """
        try:
            prompt = self._create_prompt(user_profile, context)
            response = self.model.generate_content(prompt)
            return self._format_response(response.text)
            
        except Exception as e:
            error_msg = f"Error generating advice: {str(e)}"
            print(error_msg)
            return self._get_fallback_advice(user_profile)
    
    def _create_prompt(self, user_profile: Dict, context: str) -> str:
        """Create a structured prompt for the Gemini model"""
        age = user_profile.get('age', 'unknown')
        goal = user_profile.get('goal', 'general health')
        activity_level = user_profile.get('activity_level', 'moderate')
        dietary_restrictions = user_profile.get('dietary_restrictions', [])
        
        restrictions_text = ', '.join(dietary_restrictions) if dietary_restrictions else 'None'
        
        return f"""You are a certified health and fitness coach with expertise in personalized nutrition and exercise science.

ANALYZE THIS USER PROFILE FOR PERSONALIZED ADVICE:
- Age: {age} years
- Primary Goal: {goal} (weight loss/muscle gain/endurance/overall health)
- Activity Level: {activity_level}
- Dietary Restrictions: {restrictions_text}
- Current Plan Context: {context}

For counterfactual analysis, consider:
- Basal Metabolic Rate (BMR) estimate
- Average daily caloric needs
- Recommended macronutrient ratios
- Recovery requirements
- Common plateaus and setbacks for this profile

PROVIDE EXPERT ADVICE IN THIS EXACT FORMAT:

🎯 **Key Priorities for Your Goal**
- [2-3 specific priorities tailored to their goal]

🍽️ **Nutrition Tips**
- [Specific food swaps or additions]
- [Meal timing suggestions]
- [Hydration and supplement advice if relevant]

💪 **Exercise Optimization**
- [Form tips or exercise modifications]
- [Recovery strategies]
- [Progressive overload suggestions]

⚠️ **Common Mistakes to Avoid**
- [1-2 specific pitfalls for this goal]

✅ **Quick Wins This Week**
- [3 actionable items they can start immediately]

🔍 **What If? Counterfactual Scenarios**

POSITIVE COUNTERFACTUALS (If you follow the plan):
- [1-2 alternative approaches and their potential outcomes]
- [Example: "If you increased protein intake by 20g/day, you might see 15% faster muscle recovery..."]

⚠️ **NEGATIVE COUNTERFACTUALS (If you don't follow the plan):**
- [Consequences of skipping workouts: "If you miss gym sessions 3x/week, your progress could be delayed by 2-3 weeks"]
- [Consequences of poor diet: "If you consume excess junk food (>500 cal/day), you might need an extra 1-2 weeks to reach your goal"]
- [Recovery impact: "If you skip rest days, you risk burnout and injury, requiring 3-4 weeks recovery time"]
- [Corrective actions: "To compensate, you could do 30 min extra cardio the next day OR extend your timeline by 5-7 days"]

IMPORTANT GUIDELINES:
- Be specific with numbers (portions, reps, sets, times)
- Consider their age and activity level
- Respect dietary restrictions completely
- Use encouraging, motivational language
- Keep total response under 600 words
- Use emojis for visual clarity
- Provide evidence-based recommendations
- Include both POSITIVE counterfactuals (benefits of following plan) and NEGATIVE counterfactuals (consequences of not following)
- Always provide CORRECTIVE ACTIONS for negative scenarios (extra exercise, extended timeline, etc.)
- Balance motivation with realistic consequences
"""
    
    def _format_response(self, response: str) -> str:
        """Format the model's response for better readability"""
        # Basic formatting - can be enhanced based on needs
        return response.strip()
    
    def _get_fallback_advice(self, user_profile: Dict) -> str:
        """Return fallback advice if API call fails"""
        goal = user_profile.get('goal', 'general health')
        return f"""
        I'm having trouble connecting to the AI service right now. Here's some general advice for {goal}:
        • Stay hydrated with at least 8 glasses of water daily
        • Include protein in every meal
        • Aim for 7-9 hours of quality sleep
        • Move your body for at least 30 minutes daily
        
        Please check your internet connection and try again later for personalized advice.
        """

# Example usage
if __name__ == "__main__":
    try:
        gemini = GeminiService()
        test_profile = {
            "age": 28,
            "gender": "male",
            "weight": 75,
            "height": 175,
            "activity_level": "moderately_active",
            "goal": "weight_loss",
            "dietary_restrictions": ["lactose"]
        }
        test_context = "Current plan: 1800 calories, 40% protein, 30% carbs, 30% fats, 4x weekly workouts"
        
        print("Testing Gemini integration...")
        advice = gemini.get_personalized_advice(test_profile, test_context)
        print("\nGenerated Advice:")
        print(advice)
        
    except Exception as e:
        print(f"Error in test: {e}")
        print("Please ensure you've set up your GOOGLE_API_KEY in the .env file")
