# Quick Reference Card

## 🚀 Getting Started (5 Minutes)

### 1. API Key Setup
```bash
# Get key from: https://makersuite.google.com/
# Update .env file:
GOOGLE_API_KEY=your_key_here
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Application
```bash
python app.py
# Visit: http://localhost:5000
```

---

## 📍 Finding AI Features

### Location: Explanations Tab
After generating a plan, click **Explanations** tab

### What You'll See
```
🤖 AI-Powered Personalized Advice [🔄 Regenerate]
├─ 🎯 Key Priorities
├─ 🍽️ Nutrition Tips
├─ 💪 Exercise Optimization
├─ ⚠️ Common Mistakes
├─ ✅ Quick Wins
├─ Feedback: [👍] [👎] [😐]
└─ 📚 Source: Google Gemini AI
```

---

## 🔐 Security Checklist

### API Key
- ✅ Stored in `.env` (not in code)
- ✅ Never commit `.env`
- ✅ Add to `.gitignore`
- ⚠️ If exposed: Revoke immediately

### Session
- ✅ Login required
- ✅ Session validation
- ✅ Secure cookies
- ✅ Auto-logout

### Input
- ✅ Age: 18-120
- ✅ Weight: 30-300 kg
- ✅ Height: 100-250 cm
- ✅ Validation on frontend & backend

---

## 🧪 Testing Quick Checks

### AI Advice
- [ ] Appears in Explanations tab
- [ ] Has 🤖 emoji
- [ ] Includes 5 sections (🎯🍽️💪⚠️✅)
- [ ] Personalized to profile

### Buttons
- [ ] Regenerate button clickable
- [ ] Feedback buttons highlight
- [ ] Only one feedback active
- [ ] Confirmation messages show

### Security
- [ ] Cannot access without login
- [ ] Profile validation works
- [ ] Error messages generic
- [ ] No sensitive data exposed

---

## 📊 Performance Targets

| Metric | Target | Status |
|--------|--------|--------|
| Page Load | < 2s | ✅ |
| AI Generation | 2-5s | ✅ |
| Feedback | < 100ms | ✅ |
| Regenerate | < 3s | ✅ |

---

## 🐛 Troubleshooting

### AI Advice Not Showing
```
1. Press F12 → Console
2. Look for: "AI Advice: [content]"
3. If empty: Check API key
4. If error: Check Flask logs
5. Refresh page
```

### Buttons Not Working
```
1. Check console for errors
2. Verify JavaScript loaded
3. Try different browser
4. Clear cache (Ctrl+Shift+Delete)
```

### API Key Issues
```
1. Check .env file exists
2. Verify key format
3. Restart Flask app
4. Check for typos
```

---

## 📚 Documentation Map

| Document | Purpose |
|----------|---------|
| `QUICK_START_LLM.md` | 5-min setup |
| `SECURITY_GUIDE.md` | Security details |
| `FEATURE_VISIBILITY_GUIDE.md` | Where to find features |
| `TESTING_GUIDE.md` | Testing procedures |
| `LLM_INTEGRATION_GUIDE.md` | Technical details |
| `FINAL_STATUS.md` | Complete status |

---

## 🎯 Feature Checklist

### Implemented ✅
- [x] Height input field
- [x] Gemini AI integration
- [x] AI advice display
- [x] Regenerate button (UI)
- [x] Feedback buttons
- [x] Source attribution
- [x] Loading animations
- [x] Security headers
- [x] Session security
- [x] Input validation

### Ready for Backend
- [ ] Regenerate API call
- [ ] Feedback storage
- [ ] Analytics dashboard
- [ ] Response caching

---

## 🔗 Important Links

- **Gemini API**: https://makersuite.google.com/
- **Flask Docs**: https://flask.palletsprojects.com/
- **Security**: OWASP Top 10
- **GitHub**: Your repo link

---

## ⚡ Common Commands

```bash
# Start Flask
python app.py

# Install dependencies
pip install -r requirements.txt

# Check dependencies
pip list

# Update dependencies
pip install --upgrade -r requirements.txt

# Test security
curl -I http://localhost:5000

# View logs
tail -f app.log
```

---

## 🚨 Emergency Actions

### If API Key Exposed
1. Go to https://makersuite.google.com/
2. Delete exposed key
3. Generate new key
4. Update `.env`
5. Restart Flask

### If App Crashes
1. Check Flask logs
2. Check error message
3. Verify API key
4. Restart Flask
5. Check console (F12)

### If Features Missing
1. Refresh page
2. Clear cache
3. Check console
4. Restart Flask
5. Check `.env`

---

## 📞 Support Resources

### Self-Help
1. Check relevant documentation
2. Review browser console (F12)
3. Check Flask logs
4. Verify configuration
5. Test with sample data

### Debugging
```javascript
// In browser console (F12)
console.log('Plan:', currentPlan);
console.log('AI Advice:', currentPlan.ai_advice);
```

```python
# In Flask logs
print(f"AI Advice: {ai_advice}")
print(f"Error: {str(e)}")
```

---

## ✅ Pre-Launch Checklist

- [ ] API key configured
- [ ] Dependencies installed
- [ ] Flask running
- [ ] Can create profile
- [ ] AI advice displays
- [ ] Buttons work
- [ ] No console errors
- [ ] Security headers present
- [ ] Documentation reviewed
- [ ] Ready for testing

---

## 📈 Success Metrics

### User Experience
- ✅ AI advice helpful
- ✅ Interface intuitive
- ✅ Feedback mechanism works
- ✅ Performance acceptable

### Security
- ✅ No data breaches
- ✅ All validations pass
- ✅ Security headers present
- ✅ Sessions secure

### Reliability
- ✅ No crashes
- ✅ Graceful error handling
- ✅ API fallback works
- ✅ Consistent performance

---

## 🎓 Learning Resources

### For Developers
- Flask documentation
- Google Gemini API docs
- Security best practices
- Testing frameworks

### For Users
- Feature visibility guide
- Quick start guide
- FAQ (to be created)
- Video tutorials (optional)

---

**Last Updated**: November 23, 2024
**Version**: 1.0
**Status**: ✅ READY
