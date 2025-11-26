# LLM Integration Guide - Health & Fitness XAI System

## Overview
This document provides a comprehensive guide to the Google Gemini LLM integration in the Health & Fitness XAI System.

## What Was Implemented

### 1. **LLM Service (`llm_service.py`)**
A dedicated service module that handles all interactions with Google's Gemini API.

**Key Features:**
- Structured prompt engineering for consistent, high-quality responses
- Error handling with graceful fallback advice
- Context-aware personalization based on user profile
- Formatted responses with emojis and clear structure

**Prompt Structure:**
The system uses a sophisticated prompt that includes:
- User profile analysis (age, goals, activity level, restrictions)
- Current plan context
- Specific output format requirements
- Evidence-based recommendations

### 2. **Backend Integration (`app.py`)**
Enhanced the `/get_recommendations` endpoint to include AI-powered advice.

**Flow:**
1. Generate standard recommendations
2. Retrieve user profile from database
3. Initialize Gemini service
4. Create context from the generated plan
5. Call `get_personalized_advice()`
6. Add AI advice to the response

**Error Handling:**
- Graceful degradation if API fails
- Fallback advice provided to users
- Console logging for debugging

### 3. **Frontend Enhancements (`index.html`)**

#### A. **UI Components**
- **AI Advice Section**: Dedicated display area with styling
- **Regenerate Button**: Allows users to get new advice
- **Feedback Buttons**: Collect user satisfaction (👍 Yes, 👎 No, 😐 Neutral)
- **Source Reference**: Shows that advice is from Gemini AI
- **Loading States**: Shimmer animation while generating

#### B. **CSS Animations**
```css
@keyframes slideInUp - Smooth entry animation for advice
@keyframes shimmer - Loading skeleton effect
@keyframes spin - Loading spinner animation
```

#### C. **JavaScript Functions**

**`regenerateAdvice()`**
- Triggers new advice generation
- Shows loading spinner
- Disables button during generation
- Updates content with new advice

**`submitFeedback(type)`**
- Captures user satisfaction
- Highlights selected feedback button
- Shows confirmation message
- Logs feedback for analytics

**`showAILoadingState()`**
- Displays loading animation
- Prepares UI for incoming advice

### 4. **Advanced Features**

#### A. **Structured Output Format**
The AI generates advice in this format:
```
🎯 Key Priorities for Your Goal
- [Specific priorities]

🍽️ Nutrition Tips
- [Food swaps, meal timing, hydration]

💪 Exercise Optimization
- [Form tips, recovery, progressive overload]

⚠️ Common Mistakes to Avoid
- [Goal-specific pitfalls]

✅ Quick Wins This Week
- [3 actionable items]
```

#### B. **Personalization Factors**
The system considers:
- Age and activity level
- Specific fitness goals
- Dietary restrictions
- Current plan metrics
- User's health profile

#### C. **User Feedback Loop**
- Collects satisfaction ratings
- Helps improve future recommendations
- Stored for analytics and improvement

## How to Use

### Setup

1. **Get API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/)
   - Create a new API key
   - Copy the key

2. **Configure Environment**:
   ```bash
   # Edit .env file
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Restart Flask**:
   ```bash
   python app.py
   ```

### User Workflow

1. **Create Profile**: Fill in health and fitness information
2. **Generate Plan**: System creates personalized recommendations
3. **View AI Advice**: See AI-generated insights in the "Explanations" tab
4. **Interact with Advice**:
   - Click "🔄 Regenerate" for alternative suggestions
   - Provide feedback with 👍 👎 😐 buttons
5. **Track Progress**: Use the advice to guide your fitness journey

## API Integration Details

### Endpoint: `/get_recommendations`
**Method**: GET
**Response**:
```json
{
  "success": true,
  "plan": {
    "diet_recommendations": {...},
    "exercise_recommendations": {...},
    "ai_advice": "Generated personalized advice...",
    "overall_summary": {...}
  }
}
```

### Gemini API Call
```python
gemini = GeminiService()
advice = gemini.get_personalized_advice(
    user_profile={...},
    context="Current plan summary..."
)
```

## Performance Considerations

### Rate Limiting
- Free tier: 60 requests per minute
- Monitor usage at Google AI Studio dashboard
- Implement caching for repeated queries

### Response Time
- Typical generation: 2-5 seconds
- Shows loading state to user
- Graceful fallback if timeout occurs

### Cost
- Free tier available
- No credit card required for testing
- Monitor usage for production deployment

## Future Enhancements

### Planned Features
1. **Caching System**: Store frequently requested advice
2. **Multi-language Support**: Generate advice in different languages
3. **Voice Output**: Read advice aloud
4. **Advanced Analytics**: Track which advice types are most helpful
5. **Personalized Prompting**: Adjust prompt based on user feedback
6. **Integration with Wearables**: Include real-time health data

### Potential Improvements
- Implement regenerate functionality with actual API calls
- Add feedback submission to backend
- Create admin dashboard for feedback analytics
- A/B testing different prompt variations
- Integration with other LLM providers

## Troubleshooting

### Common Issues

**Issue**: "GOOGLE_API_KEY not found"
- **Solution**: Check `.env` file has correct key format
- Ensure `.env` is in project root directory

**Issue**: API timeout or slow responses
- **Solution**: Check internet connection
- Verify API key is valid
- Check rate limits haven't been exceeded

**Issue**: Advice not appearing
- **Solution**: Check browser console for errors
- Verify backend is running
- Check that user profile is complete

**Issue**: Regenerate button not working
- **Solution**: Currently shows placeholder message
- Implement actual API call in production
- Ensure user is logged in

## Code Examples

### Using the LLM Service Directly
```python
from llm_service import GeminiService

gemini = GeminiService()
user_profile = {
    "age": 28,
    "goal": "weight_loss",
    "activity_level": "moderately_active",
    "dietary_restrictions": ["gluten-free"]
}
context = "1800 cal/day, 40% protein, 3x weekly workouts"

advice = gemini.get_personalized_advice(user_profile, context)
print(advice)
```

### Handling Errors
```python
try:
    advice = gemini.get_personalized_advice(profile, context)
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"API error: {e}")
    # Use fallback advice
```

## Security Best Practices

1. **API Key Management**:
   - Never commit `.env` to version control
   - Use environment variables in production
   - Rotate keys periodically

2. **Data Privacy**:
   - Don't log sensitive user data
   - Comply with data protection regulations
   - Secure user feedback storage

3. **Rate Limiting**:
   - Implement server-side rate limiting
   - Prevent API abuse
   - Monitor unusual patterns

## Monitoring and Analytics

### Key Metrics to Track
- Average response time
- API error rate
- User feedback distribution
- Most common advice types
- Regenerate button usage

### Logging
```python
# Enable logging in llm_service.py
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

## Support and Resources

- **Google Gemini Docs**: https://ai.google.dev/
- **API Reference**: https://ai.google.dev/api/python
- **Community**: Google AI Discord/Forums
- **Issues**: Check GitHub issues for known problems

## Version History

- **v1.0** (Nov 2024): Initial LLM integration with Gemini
  - Basic advice generation
  - User feedback collection
  - Loading states and animations
  - Regenerate functionality (placeholder)

## License
This integration follows the same license as the main Health & Fitness XAI System.

---

**Last Updated**: November 23, 2024
**Maintained By**: Health & Fitness XAI Team
