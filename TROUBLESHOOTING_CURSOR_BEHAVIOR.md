# Troubleshooting Cursor Behavior
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

## 🔧 When Cursor Doesn't Follow SpecFirst Behavior

### **Problem**: Cursor generates code immediately instead of refining specifications

### **Expected Behavior**:
```
🎯 I'll help you build this using Agile SpecFirst methodology!
[Specification refinement questions]
```

### **Wrong Behavior**:
```python
# Cursor starts writing code immediately
from flask import Flask
app = Flask(__name__)
```

## 🔍 Diagnostic Steps

### 1. **Check .cursorrules Location**
```bash
ls -la .cursorrules
# Should show the file exists in project root
```

### 2. **Verify .cursorrules Content**
```bash
head -20 .cursorrules
# Should show the immediate behavior instructions at the top
```

### 3. **Check File Size**
```bash
wc -l .cursorrules
# Should show ~330+ lines
```

### 4. **Restart Cursor**
- Close Cursor completely
- Reopen Cursor
- Open this project
- Try test query again

### 5. **Clear Cursor Cache** (if option available)
- Check Cursor settings for cache clearing
- Or restart with fresh workspace

## 🧪 Test Cases

### **Test 1**: Simple Request
**Input**: "I want to build a web app"

**Expected Response**:
```
🎯 I'll help you build this using Agile SpecFirst methodology!

Let me understand your vision:
- You want a web application
- This sounds like a [type] project
- You'll likely need [observation]

First, let's refine your specifications before any implementation.

📝 I need to understand:
- WHO will use this application?
- WHAT are the core user workflows?
- HOW should users interact with the system?
- WHAT are your success criteria?
- ANY technical constraints or preferences?
```

### **Test 2**: Vague Request
**Input**: "I need help with something"

**Expected**: Should ask clarifying questions about what they want to build

### **Test 3**: Specific Request
**Input**: "Create a Flask API for user authentication"

**Expected**: Should still ask about requirements before generating code

## 🔧 Fixes

### **Fix 1**: Ensure .cursorrules is in project root
```bash
# Make sure you're in the right directory
pwd
# Should show path ending in /basic_llm

# Check if .cursorrules exists
ls -la .cursorrules
```

### **Fix 2**: Check for syntax errors in .cursorrules
```bash
# Look for any obvious formatting issues
cat .cursorrules | head -50
```

### **Fix 3**: Try in a new Cursor chat tab
- Open new chat tab in same project
- Test with simple query
- Compare behavior

### **Fix 4**: Check Cursor workspace settings
- Ensure Cursor is reading from correct workspace
- Verify no conflicting configuration files

## 🎯 Success Indicators

### **You know it's working when**:
✅ No code appears in initial responses  
✅ Cursor asks about user requirements  
✅ Mentions "Agile SpecFirst methodology"  
✅ Asks WHO, WHAT, HOW, SUCCESS questions  
✅ Feels like consulting with a software engineer  

### **Red flags (still broken)**:
❌ Immediate code blocks  
❌ Technology choices without asking  
❌ Implementation without requirements  
❌ No mention of specification refinement  

## 📞 Additional Help

### **If still not working**:
1. **Copy .cursorrules to new project** - Test if behavior works elsewhere
2. **Check Cursor version** - Ensure you have recent version
3. **Try different file location** - Some Cursor versions read from different paths
4. **Manual verification** - Ask Cursor "What development methodology should you follow in this project?"

### **Working Response Should Include**:
- Reference to "Agile SpecFirst"
- Mention of specification refinement
- Requirement gathering questions
- No immediate code generation

---

**Quick Test**: Open new Cursor chat, type "build me something", see if you get specification questions instead of code. 