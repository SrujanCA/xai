# Feedback System Testing Guide

## Quick Start Testing

### 1. Start the Application
```bash
python app.py
```

### 2. Login
- Navigate to `http://127.0.0.1:5000`
- Login with credentials:
  - Email: `admin@123.com`
  - Password: `admin123`

### 3. View Recommendations
- Create a profile or use existing profile
- Navigate to the recommendations section
- Scroll down to see the AI advice section

### 4. Test Feedback Buttons
- Click one of the feedback buttons:
  - 👍 Yes (helpful)
  - 👎 No (not-helpful)
  - 😐 Neutral

### 5. Verify Feedback Submission
- You should see a confirmation message
- Check the browser console (F12) for logs
- Verify `feedback_db.json` file is created/updated

## Testing Scenarios

### Scenario 1: Submit Helpful Feedback
1. Click the 👍 Yes button
2. Expected: Green confirmation message appears
3. Expected: Button highlights
4. Expected: Feedback stored in database

### Scenario 2: Submit Not Helpful Feedback
1. Click the 👎 No button
2. Expected: Blue confirmation message appears
3. Expected: Button highlights
4. Expected: Feedback stored in database

### Scenario 3: Submit Neutral Feedback
1. Click the 😐 Neutral button
2. Expected: Orange confirmation message appears
3. Expected: Button highlights
4. Expected: Feedback stored in database

### Scenario 4: View Feedback Statistics (Admin)
1. Login as admin
2. Navigate to: `http://127.0.0.1:5000/feedback-stats`
3. Expected: JSON response with feedback statistics
4. Example response:
```json
{
  "success": true,
  "stats": {
    "total": 3,
    "helpful": 2,
    "not_helpful": 1,
    "neutral": 0
  }
}
```

### Scenario 5: View Enhanced Cards
1. Navigate to recommendations
2. Scroll to "📋 Why This Works For You" section
3. Expected: Cards displayed in grid layout
4. Expected: Cards have emojis and titles:
   - 🎯 Key Priorities for Your Goal
   - 🍽️ Nutrition Tips
   - 💪 Exercise Optimization
   - ⚠️ Common Mistakes to Avoid
   - ✅ Quick Wins This Week
   - 🔍 What If? Counterfactual Scenarios

### Scenario 6: Test Card Hover Effects
1. Hover over any card
2. Expected: Card lifts up (translateY effect)
3. Expected: Background becomes brighter
4. Expected: Shadow increases

## Database Verification

### Check Feedback Database
1. Open `feedback_db.json` in the project root
2. Verify structure:
```json
[
  {
    "user_email": "admin@123.com",
    "feedback_type": "helpful",
    "advice_text": "...",
    "detailed_comment": null,
    "timestamp": "2025-11-23T18:07:00.000000"
  }
]
```

### Verify Feedback Count
- Each feedback submission should add a new entry
- Timestamps should be unique
- User email should match logged-in user

## Error Testing

### Test 1: Submit Feedback Without Login
1. Clear browser cookies/session
2. Try to submit feedback via browser console:
```javascript
fetch('/submit-feedback', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({type: 'helpful'})
})
```
3. Expected: 401 error "Please login first"

### Test 2: Access Stats Without Admin
1. Login as regular user
2. Navigate to: `http://127.0.0.1:5000/feedback-stats`
3. Expected: 403 error "Admin access required"

### Test 3: Submit Invalid Feedback Type
1. Via browser console:
```javascript
fetch('/submit-feedback', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({type: 'invalid'})
})
```
2. Expected: Still stores (no validation on type)
3. Note: Consider adding validation in production

## Browser Console Testing

### Check for Errors
1. Open Developer Tools (F12)
2. Go to Console tab
3. Submit feedback
4. Expected: No errors
5. Expected: Log message: "Feedback submitted: [type] {data}"

### Check Network Requests
1. Open Developer Tools (F12)
2. Go to Network tab
3. Submit feedback
4. Expected: POST request to `/submit-feedback`
5. Expected: Response status 200
6. Expected: Response body contains success message

## Performance Testing

### Test 1: Multiple Feedback Submissions
1. Submit 5-10 feedback entries
2. Expected: No performance degradation
3. Expected: All entries stored correctly
4. Check `feedback_db.json` size

### Test 2: Load Statistics
1. With 100+ feedback entries
2. Navigate to `/feedback-stats`
3. Expected: Response time < 1 second
4. Expected: Accurate counts

## UI/UX Testing

### Test 1: Button States
- **Normal**: Transparent with white border
- **Hover**: Slightly opaque with glow
- **Active**: Highlighted with full opacity
- **After Click**: Maintains highlight

### Test 2: Card Responsiveness
- **Desktop**: 3 cards per row
- **Tablet**: 2 cards per row
- **Mobile**: 1 card per row
- Test by resizing browser window

### Test 3: Confirmation Messages
- **Helpful**: "👍 Thanks! We're glad the advice was helpful..."
- **Not Helpful**: "👎 We'll work on improving..."
- **Neutral**: "😐 Thanks for the feedback!..."

## Checklist

- [ ] Feedback buttons display correctly
- [ ] Feedback submission works without errors
- [ ] Confirmation messages appear
- [ ] Database file is created
- [ ] Feedback entries are stored correctly
- [ ] Admin can view statistics
- [ ] Non-admin cannot view statistics
- [ ] Cards display in grid layout
- [ ] Cards have correct emojis and titles
- [ ] Hover effects work on cards
- [ ] Responsive design works on mobile
- [ ] No console errors
- [ ] Network requests are successful

## Troubleshooting

### Issue: Feedback not storing
- Check if `feedback_db.json` is writable
- Verify user is logged in
- Check browser console for errors
- Verify `/submit-feedback` endpoint is accessible

### Issue: Cards not displaying
- Clear browser cache
- Hard refresh (Ctrl+Shift+R)
- Check browser console for CSS errors
- Verify CSS is loaded correctly

### Issue: Statistics endpoint not working
- Verify logged in as admin
- Check admin credentials: `admin@123.com` / `admin123`
- Verify `/feedback-stats` endpoint exists
- Check browser console for errors

### Issue: Confirmation messages not showing
- Verify alert container exists in DOM
- Check CSS for alert styling
- Verify `showAlert()` function is defined
- Check browser console for errors

## Next Steps

After testing:
1. Document any issues found
2. Test on different browsers (Chrome, Firefox, Safari, Edge)
3. Test on different devices (desktop, tablet, mobile)
4. Gather user feedback
5. Plan additional enhancements
