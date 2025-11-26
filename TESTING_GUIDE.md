# Testing Guide - LLM Integration

## Overview
This guide provides comprehensive testing procedures for the Gemini LLM integration in the Health & Fitness XAI System.

---

## Pre-Testing Setup

### Requirements
- Python 3.8+
- Flask running locally
- Google Gemini API key
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection

### Verification Checklist
```bash
# Check Python version
python --version

# Check Flask installation
pip list | grep Flask

# Check dependencies
pip list | grep google-generativeai

# Verify .env file exists
ls -la .env

# Check Flask is running
curl http://localhost:5000
```

---

## Test Suite 1: Setup & Configuration

### Test 1.1: API Key Configuration
**Objective**: Verify API key is correctly configured
**Steps**:
1. Open `.env` file
2. Verify `GOOGLE_API_KEY` is set
3. Verify key format (should start with `sk-` or similar)
4. Restart Flask app

**Expected Result**: ✅ No errors in console

**Failure Handling**:
- If error: "GOOGLE_API_KEY not found"
  - Check `.env` file exists in project root
  - Verify key is not wrapped in quotes
  - Restart Flask

### Test 1.2: Dependencies Installation
**Objective**: Verify all required packages installed
**Steps**:
```bash
pip install -r requirements.txt
```

**Expected Result**: ✅ All packages installed successfully

**Verify**:
```bash
python -c "import google.generativeai; print('✓ google-generativeai installed')"
python -c "from dotenv import load_dotenv; print('✓ python-dotenv installed')"
```

### Test 1.3: Flask Application Start
**Objective**: Verify Flask starts without errors
**Steps**:
1. Open terminal
2. Run: `python app.py`
3. Wait for "Running on http://0.0.0.0:5000"

**Expected Result**: ✅ Flask running without errors

**Check Console**:
- No "ImportError" messages
- No "GOOGLE_API_KEY" errors
- Server listening on port 5000

---

## Test Suite 2: Frontend Features

### Test 2.1: Height Input Field
**Objective**: Verify height field is present and functional
**Steps**:
1. Navigate to http://localhost:5000
2. Look for "Create Your Profile" form
3. Locate "Height (cm)" field
4. Enter value: 175

**Expected Result**: ✅ Field accepts values between 100-250

**Test Cases**:
- Valid: 150, 175, 200 ✓
- Invalid: 50 (too low) ✗
- Invalid: 300 (too high) ✗
- Decimal: 175.5 ✓

### Test 2.2: Profile Form Submission
**Objective**: Verify profile can be created with height
**Steps**:
1. Fill complete profile:
   - Name: Test User
   - Age: 28
   - Gender: Male
   - Weight: 75 kg
   - **Height: 175 cm** ← NEW
   - Activity Level: Moderately Active
   - Sleep: 7 hours
   - Goals: Weight Loss
2. Click "Generate Plan"

**Expected Result**: ✅ Plan generated successfully

**Verify**:
- No form validation errors
- Plan displays in results section
- Height used in calculations (BMI, etc.)

### Test 2.3: AI Advice Display
**Objective**: Verify AI advice appears in Explanations tab
**Steps**:
1. After plan generation, click "Explanations" tab
2. Look for "🤖 AI-Powered Personalized Advice" section
3. Verify advice content is visible

**Expected Result**: ✅ AI advice displays with proper formatting

**Verify**:
- Advice appears at top of Explanations tab
- Contains emojis (🎯 🍽️ 💪 ⚠️ ✅)
- Text is readable and formatted
- Source reference shows "Google Gemini AI"

### Test 2.4: Regenerate Button
**Objective**: Verify regenerate button is present and clickable
**Steps**:
1. In AI advice section, locate "🔄 Regenerate" button
2. Click the button
3. Observe loading state

**Expected Result**: ✅ Button shows loading animation

**Verify**:
- Button is clickable
- Loading spinner appears
- Button text changes to "Regenerating..."
- After 2 seconds, button resets

### Test 2.5: Feedback Buttons
**Objective**: Verify feedback buttons work
**Steps**:
1. In AI advice section, find feedback buttons
2. Click "👍 Yes"
3. Observe button state change

**Expected Result**: ✅ Button highlights and shows confirmation

**Test All Buttons**:
- 👍 Yes: "Thanks! We're glad the advice was helpful."
- 👎 No: "We'll work on improving the recommendations."
- 😐 Neutral: "Thanks for the feedback!"

**Verify**:
- Button highlights when clicked
- Confirmation message appears
- Only one button active at a time

### Test 2.6: Loading Animations
**Objective**: Verify animations display smoothly
**Steps**:
1. Generate a new plan
2. Watch for loading states
3. Observe transitions

**Expected Result**: ✅ Smooth animations without jank

**Verify**:
- Shimmer animation on loading
- Slide-in animation for advice
- Spinner rotates smoothly
- No console errors

---

## Test Suite 3: AI Functionality

### Test 3.1: Personalization
**Objective**: Verify advice is personalized to user
**Steps**:
1. Create profile with:
   - Goal: Weight Loss
   - Activity: Sedentary
2. Generate plan
3. Check AI advice

**Expected Result**: ✅ Advice tailored to weight loss goal

**Verify**:
- Mentions caloric deficit
- Suggests appropriate exercise level
- Respects sedentary activity level
- Includes relevant nutrition tips

### Test 3.2: Dietary Restrictions
**Objective**: Verify advice respects dietary restrictions
**Steps**:
1. Create profile with:
   - Dietary Restriction: Vegetarian
2. Generate plan
3. Check AI advice

**Expected Result**: ✅ Advice respects vegetarian diet

**Verify**:
- No meat recommendations
- Suggests plant-based proteins
- Mentions alternative foods
- Acknowledges dietary choice

### Test 3.3: Age Consideration
**Objective**: Verify advice considers user age
**Steps**:
1. Create profile with:
   - Age: 45
2. Generate plan
3. Check AI advice

**Expected Result**: ✅ Advice appropriate for age

**Verify**:
- Mentions recovery considerations
- Suggests appropriate intensity
- Includes injury prevention tips
- Age-appropriate recommendations

### Test 3.4: Goal-Specific Advice
**Objective**: Verify advice matches fitness goal
**Steps**:
1. Create profile with:
   - Goal: Muscle Gain
2. Generate plan
3. Check AI advice

**Expected Result**: ✅ Advice focused on muscle building

**Verify**:
- Emphasizes protein intake
- Suggests strength training
- Mentions progressive overload
- Includes recovery nutrition

### Test 3.5: Response Quality
**Objective**: Verify advice quality and relevance
**Steps**:
1. Generate plan
2. Read through AI advice
3. Evaluate content

**Expected Result**: ✅ Advice is relevant and actionable

**Checklist**:
- [ ] Specific numbers provided (reps, sets, calories)
- [ ] Actionable recommendations
- [ ] Evidence-based suggestions
- [ ] Encouraging tone
- [ ] Clear structure with sections
- [ ] Relevant to user profile

---

## Test Suite 4: Error Handling

### Test 4.1: Invalid API Key
**Objective**: Verify graceful handling of invalid API key
**Steps**:
1. Edit `.env`: `GOOGLE_API_KEY=invalid_key_12345`
2. Restart Flask
3. Generate a plan

**Expected Result**: ✅ Fallback advice shown, no crash

**Verify**:
- No application error
- Fallback advice displays
- Console shows warning message
- User can continue using app

### Test 4.2: Network Timeout
**Objective**: Verify handling of API timeout
**Steps**:
1. Disconnect internet (or use network throttling)
2. Generate a plan
3. Wait for timeout

**Expected Result**: ✅ Fallback advice shown after timeout

**Verify**:
- Timeout handled gracefully
- Fallback advice displayed
- User notified of issue
- No console errors

### Test 4.3: Missing API Key
**Objective**: Verify error message for missing key
**Steps**:
1. Delete `.env` file
2. Restart Flask
3. Try to generate plan

**Expected Result**: ✅ Clear error message shown

**Verify**:
- Error message is helpful
- Suggests solution (get API key)
- Provides link to Google AI Studio
- Application doesn't crash

### Test 4.4: Incomplete Profile
**Objective**: Verify handling of incomplete profile
**Steps**:
1. Try to submit form with missing fields
2. Leave Height field empty
3. Click Generate Plan

**Expected Result**: ✅ Validation error shown

**Verify**:
- Required field validation works
- Height field is required
- Error message is clear
- Form doesn't submit

---

## Test Suite 5: Performance

### Test 5.1: Response Time
**Objective**: Measure AI advice generation time
**Steps**:
1. Open browser DevTools (F12)
2. Go to Network tab
3. Generate a plan
4. Check request time

**Expected Result**: ✅ Response time < 5 seconds

**Measure**:
- API call duration
- Total page load time
- AI advice generation time

**Acceptable Times**:
- Fast: < 2 seconds
- Normal: 2-4 seconds
- Slow: 4-5 seconds
- Timeout: > 5 seconds

### Test 5.2: UI Responsiveness
**Objective**: Verify UI remains responsive during loading
**Steps**:
1. Generate a plan
2. While loading, try to interact with page
3. Click buttons, scroll, etc.

**Expected Result**: ✅ UI remains responsive

**Verify**:
- Page scrolls smoothly
- Buttons are clickable
- No freezing or lag
- Animations are smooth

### Test 5.3: Memory Usage
**Objective**: Check for memory leaks
**Steps**:
1. Open DevTools (F12)
2. Go to Memory tab
3. Generate multiple plans
4. Check memory usage

**Expected Result**: ✅ No significant memory increase

**Verify**:
- Memory doesn't grow unbounded
- No memory leaks detected
- Garbage collection working
- Performance stable

### Test 5.4: Concurrent Users
**Objective**: Verify system handles multiple users
**Steps**:
1. Open multiple browser windows
2. Generate plans in each simultaneously
3. Monitor performance

**Expected Result**: ✅ All requests handled properly

**Verify**:
- All plans generate successfully
- No race conditions
- Responses are accurate
- No data mixing between users

---

## Test Suite 6: Browser Compatibility

### Test 6.1: Chrome
**Steps**:
1. Open Chrome
2. Navigate to http://localhost:5000
3. Test all features

**Expected Result**: ✅ All features work

### Test 6.2: Firefox
**Steps**:
1. Open Firefox
2. Navigate to http://localhost:5000
3. Test all features

**Expected Result**: ✅ All features work

### Test 6.3: Safari
**Steps**:
1. Open Safari
2. Navigate to http://localhost:5000
3. Test all features

**Expected Result**: ✅ All features work

### Test 6.4: Mobile Browser
**Steps**:
1. Open mobile device
2. Navigate to http://localhost:5000
3. Test responsive design

**Expected Result**: ✅ Mobile layout works properly

**Verify**:
- Responsive design adapts
- Touch interactions work
- Text is readable
- No horizontal scrolling

---

## Test Suite 7: Data Validation

### Test 7.1: Height Validation
**Test Cases**:
```
Input | Expected | Result
------|----------|--------
100   | Accept   | ✓
175   | Accept   | ✓
250   | Accept   | ✓
99    | Reject   | ✗
251   | Reject   | ✗
0     | Reject   | ✗
-175  | Reject   | ✗
```

### Test 7.2: Profile Data Validation
**Test Cases**:
```
Field | Valid | Invalid
------|-------|----------
Age   | 20-80 | <18, >120
Weight| 30-300| <30, >300
Height| 100-250| <100, >250
```

### Test 7.3: Form Submission
**Test Cases**:
- All fields filled: ✓ Submit
- Missing required field: ✗ Show error
- Invalid data type: ✗ Show error
- Out of range: ✗ Show error

---

## Test Suite 8: Integration Tests

### Test 8.1: End-to-End Flow
**Steps**:
1. Start fresh browser session
2. Create new profile with height
3. Generate plan
4. View AI advice
5. Provide feedback
6. Try regenerate

**Expected Result**: ✅ Complete flow works

### Test 8.2: Data Persistence
**Steps**:
1. Create profile
2. Generate plan
3. Refresh page
4. Check if plan still visible

**Expected Result**: ✅ Data persists in session

### Test 8.3: Multiple Plans
**Steps**:
1. Create profile A
2. Generate plan
3. Create profile B
4. Generate plan
5. Check both plans are correct

**Expected Result**: ✅ Plans don't interfere

---

## Test Results Template

```markdown
## Test Run: [Date]

### Setup Tests
- [ ] Test 1.1: API Key Configuration - PASS/FAIL
- [ ] Test 1.2: Dependencies Installation - PASS/FAIL
- [ ] Test 1.3: Flask Application Start - PASS/FAIL

### Frontend Tests
- [ ] Test 2.1: Height Input Field - PASS/FAIL
- [ ] Test 2.2: Profile Form Submission - PASS/FAIL
- [ ] Test 2.3: AI Advice Display - PASS/FAIL
- [ ] Test 2.4: Regenerate Button - PASS/FAIL
- [ ] Test 2.5: Feedback Buttons - PASS/FAIL
- [ ] Test 2.6: Loading Animations - PASS/FAIL

### AI Functionality Tests
- [ ] Test 3.1: Personalization - PASS/FAIL
- [ ] Test 3.2: Dietary Restrictions - PASS/FAIL
- [ ] Test 3.3: Age Consideration - PASS/FAIL
- [ ] Test 3.4: Goal-Specific Advice - PASS/FAIL
- [ ] Test 3.5: Response Quality - PASS/FAIL

### Error Handling Tests
- [ ] Test 4.1: Invalid API Key - PASS/FAIL
- [ ] Test 4.2: Network Timeout - PASS/FAIL
- [ ] Test 4.3: Missing API Key - PASS/FAIL
- [ ] Test 4.4: Incomplete Profile - PASS/FAIL

### Performance Tests
- [ ] Test 5.1: Response Time - PASS/FAIL
- [ ] Test 5.2: UI Responsiveness - PASS/FAIL
- [ ] Test 5.3: Memory Usage - PASS/FAIL
- [ ] Test 5.4: Concurrent Users - PASS/FAIL

### Browser Compatibility
- [ ] Test 6.1: Chrome - PASS/FAIL
- [ ] Test 6.2: Firefox - PASS/FAIL
- [ ] Test 6.3: Safari - PASS/FAIL
- [ ] Test 6.4: Mobile - PASS/FAIL

### Data Validation
- [ ] Test 7.1: Height Validation - PASS/FAIL
- [ ] Test 7.2: Profile Data Validation - PASS/FAIL
- [ ] Test 7.3: Form Submission - PASS/FAIL

### Integration Tests
- [ ] Test 8.1: End-to-End Flow - PASS/FAIL
- [ ] Test 8.2: Data Persistence - PASS/FAIL
- [ ] Test 8.3: Multiple Plans - PASS/FAIL

### Summary
- **Total Tests**: 31
- **Passed**: __
- **Failed**: __
- **Success Rate**: __%

### Notes
[Add any observations, issues, or comments]
```

---

## Debugging Tips

### Check Browser Console
```javascript
// Open DevTools: F12
// Go to Console tab
// Look for errors
```

### Check Flask Logs
```bash
# Terminal output shows:
# - Request logs
# - Error messages
# - API call details
```

### Enable Debug Logging
```python
# In llm_service.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Test API Key Directly
```python
from llm_service import GeminiService

try:
    gemini = GeminiService()
    print("✓ API key valid")
except Exception as e:
    print(f"✗ Error: {e}")
```

---

## Common Issues & Solutions

### Issue: "GOOGLE_API_KEY not found"
**Solution**:
1. Check `.env` exists in project root
2. Verify key format
3. Restart Flask
4. Check for typos

### Issue: AI advice not appearing
**Solution**:
1. Check browser console (F12)
2. Verify Flask is running
3. Check API key is valid
4. Wait 2-5 seconds for response

### Issue: Slow response time
**Solution**:
1. Check internet connection
2. Verify API key is valid
3. Check rate limits
4. Try again in a few seconds

### Issue: Feedback buttons not working
**Solution**:
1. Check JavaScript console for errors
2. Verify buttons are visible
3. Try refreshing page
4. Check browser compatibility

---

## Performance Benchmarks

### Target Metrics
- Page load: < 2 seconds
- AI advice generation: 2-5 seconds
- Feedback submission: < 100ms
- Regenerate action: < 3 seconds

### Acceptable Ranges
- Fast: < 2 seconds
- Normal: 2-4 seconds
- Slow: 4-5 seconds
- Timeout: > 5 seconds

---

## Sign-Off

**Tested By**: _______________
**Date**: _______________
**Status**: ✅ PASS / ❌ FAIL
**Notes**: _______________

---

**Last Updated**: November 23, 2024
**Version**: 1.0
