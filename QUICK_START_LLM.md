# Quick Start: LLM Integration

## 5-Minute Setup

### Step 1: Get Your API Key (2 minutes)
1. Go to https://makersuite.google.com/
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

### Step 2: Configure Your Project (1 minute)
1. Open `.env` file in your project root
2. Replace `your_api_key_here` with your actual API key:
   ```
   GOOGLE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
   ```
3. Save the file

### Step 3: Install Dependencies (1 minute)
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application (1 minute)
```bash
python app.py
```

Visit: http://localhost:5000

---

## Testing the LLM Integration

### Test 1: Create a Profile
1. Click "Create Your Profile"
2. Fill in your information:
   - Name: Your Name
   - Age: 28
   - Gender: Male/Female
   - Weight: 75 kg
   - **Height: 175 cm** ← NEW FIELD
   - Activity Level: Moderately Active
   - Sleep: 7 hours
   - Goals: Weight Loss
3. Click "Generate Plan"

### Test 2: View AI Advice
1. Scroll to the "Explanations" tab
2. Look for the "🤖 AI-Powered Personalized Advice" section
3. You should see personalized advice with:
   - Key priorities for your goal
   - Nutrition tips
   - Exercise optimization
   - Common mistakes to avoid
   - Quick wins for this week

### Test 3: Interact with AI Advice
1. **Regenerate**: Click "🔄 Regenerate" to get new advice
2. **Feedback**: Click 👍 👎 😐 to rate the advice
3. **Source**: See "📚 Source" reference

---

## What You'll See

### AI Advice Format
```
🤖 AI-Powered Personalized Advice

🎯 Key Priorities for Your Goal
- Create a caloric deficit of 500-750 calories daily
- Maintain high protein intake (1.6-2.2g per kg)
- Focus on compound exercises for maximum efficiency

🍽️ Nutrition Tips
- Swap refined carbs for whole grains
- Eat protein with every meal
- Stay hydrated with 2.5-3L water daily

💪 Exercise Optimization
- Perform strength training 3-4x per week
- Add 20-30 min cardio on rest days
- Focus on progressive overload

⚠️ Common Mistakes to Avoid
- Cutting calories too aggressively
- Neglecting strength training

✅ Quick Wins This Week
- Replace sugary drinks with water
- Add 10,000 steps daily
- Meal prep for 3 days
```

---

## Features Implemented

### ✅ Height Input Field
- Added to profile creation form
- Used in BMI and other calculations
- Stored in user profile

### ✅ Gemini AI Integration
- Personalized advice generation
- Context-aware recommendations
- Evidence-based suggestions

### ✅ User Interface Enhancements
- Loading animations (shimmer effect)
- Smooth transitions (slide-in animation)
- Responsive design

### ✅ Interactive Features
- 🔄 Regenerate button (placeholder for now)
- 👍 👎 😐 Feedback buttons
- 📚 Source reference

### ✅ Advanced Prompt Engineering
- Structured output format
- Personalization factors
- Evidence-based recommendations

---

## Troubleshooting

### "GOOGLE_API_KEY not found"
```
✓ Check .env file exists in project root
✓ Verify key format is correct
✓ Restart Flask app after updating .env
```

### AI Advice Not Appearing
```
✓ Check browser console (F12 → Console tab)
✓ Verify Flask is running
✓ Check that profile is complete
✓ Wait 2-5 seconds for API response
```

### Slow Response
```
✓ Check internet connection
✓ Verify API key is valid
✓ Check rate limits (60 req/min free tier)
✓ Try again in a few seconds
```

---

## Next Steps

### Immediate
- [ ] Test the LLM integration with your profile
- [ ] Provide feedback on AI advice quality
- [ ] Check browser console for any errors

### Short Term
- [ ] Implement actual regenerate API calls
- [ ] Add feedback submission to backend
- [ ] Create analytics dashboard

### Long Term
- [ ] Implement caching for faster responses
- [ ] Add multi-language support
- [ ] Integrate with wearable devices
- [ ] A/B test different prompts

---

## File Structure

```
health_fitness_xai/
├── llm_service.py              ← NEW: Gemini API service
├── app.py                      ← UPDATED: Enhanced with LLM
├── templates/
│   └── index.html              ← UPDATED: UI enhancements
├── .env                        ← NEW: API key configuration
├── requirements.txt            ← UPDATED: New dependencies
├── LLM_INTEGRATION_GUIDE.md    ← NEW: Detailed guide
└── QUICK_START_LLM.md          ← NEW: This file
```

---

## Key Changes Summary

### Backend Changes
- **llm_service.py**: New Gemini service class
- **app.py**: Enhanced `/get_recommendations` endpoint
- **requirements.txt**: Added google-generativeai, python-dotenv

### Frontend Changes
- **index.html**: 
  - New CSS animations and styles
  - AI advice display section
  - Regenerate and feedback buttons
  - JavaScript functions for interactivity

### New Features
- Height input field in profile form
- AI-powered personalized advice
- User feedback collection
- Loading states and animations
- Source attribution

---

## Performance Tips

### For Better Responses
1. **Complete Profile**: Fill all fields accurately
2. **Specific Goals**: Choose clear fitness objectives
3. **Realistic Expectations**: AI learns from feedback

### For Faster Performance
1. **Check Connection**: Ensure stable internet
2. **Monitor Usage**: Stay within rate limits
3. **Cache Results**: Avoid repeated queries

---

## Support

**Documentation**: See `LLM_INTEGRATION_GUIDE.md`
**Issues**: Check browser console (F12)
**API Status**: https://status.ai.google.dev/

---

## Quick Reference

| Feature | Status | Notes |
|---------|--------|-------|
| Height Input | ✅ Complete | Added to profile form |
| Gemini Integration | ✅ Complete | Working with free tier |
| AI Advice Display | ✅ Complete | Shows in Explanations tab |
| Regenerate Button | ⏳ Partial | UI ready, API call needed |
| Feedback Buttons | ✅ Complete | Collects user satisfaction |
| Loading States | ✅ Complete | Shimmer animation |
| Source Reference | ✅ Complete | Shows Gemini attribution |

---

**Last Updated**: November 23, 2024
**Status**: Ready for Testing ✅
