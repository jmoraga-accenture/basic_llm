# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Expected Behavior Test for Agile SpecFirst Framework

This document shows exactly what should happen when a user starts a new Cursor Chat conversation after implementing the Agile SpecFirst framework.

## 🧪 **Test Scenario 1: Simple Web App Request**

### **User Input:**
```
"I want to build a web app to track my reading list"
```

### **Expected Cursor Response (NEW BEHAVIOR):**
```
🎯 I'll help you build this using Agile SpecFirst methodology!

Let me understand your vision:
- You want a web app for tracking reading lists
- This sounds like a personal productivity tool
- You'll likely want to add, view, and manage books

First, let's refine your specifications before any implementation.

📝 Let's create your specifications.txt → SPECIFICATIONS.md

I need to understand:
- WHO will use this application? (Just you, family, public?)
- WHAT are the core user workflows? (Add books, mark as read, search, etc.)
- HOW should users interact with the system? (Web interface, mobile-friendly?)
- WHAT are your success criteria? (How do you know it's working well?)
- ANY technical constraints or preferences? (Local vs cloud, specific technologies?)

Let me know these details and I'll help structure your complete specification!
```

### **OLD BEHAVIOR (What we DON'T want to see):**
```
I'll help you build a reading list web app. Let me create a Flask application for you:

```python
from flask import Flask, render_template
app = Flask(__name__)
# ... immediate code generation
```

## 🧪 **Test Scenario 2: AI Tool Request**

### **User Input:**
```
"Create a tool that generates code snippets using AI"
```

### **Expected Cursor Response (NEW BEHAVIOR):**
```
🎯 I'll help you build this using Agile SpecFirst methodology!

What I understand: You want an AI-powered code generation tool

Let's refine your specifications first:

1. **Which programming languages** should it generate? (Python, JavaScript, etc.)
2. **What type of code snippets?** (Functions, classes, complete modules?)
3. **How do users describe what they want?** (Natural language, examples, templates?)
4. **What AI service should power this?** (OpenAI, local model, specific API?)
5. **Where should this run?** (Web app, desktop tool, CLI?)

These details ensure:
- The application works reliably in real-world scenarios
- All user needs are addressed  
- The implementation is production-ready

Once we have clear specifications, I'll generate your production-ready application.
```

## 🧪 **Test Scenario 3: Vague Request**

### **User Input:**
```
"I need something to help with my work"
```

### **Expected Cursor Response (NEW BEHAVIOR):**
```
🎯 I'll help you build this using Agile SpecFirst methodology!

Let me understand your vision:
- You need a work-related tool
- This could be productivity, automation, data processing, or communication

📝 I need a bit more detail to create complete specifications:

**Missing pieces**:
- What specific work challenge are you trying to solve?
- What does your current workflow look like?
- Who else might use this tool?
- What would success look like for you?

**These details ensure**:
- The application works reliably in real-world scenarios
- All user needs are addressed
- The implementation is production-ready

Could you describe more about what aspect of your work you'd like to improve?
```

## ✅ **Testing Checklist**

### **Behavior Validation Checklist:**
- [ ] **No immediate code generation** - Cursor should NOT jump straight to writing code
- [ ] **Specification refinement questions** - Should ask clarifying questions about requirements
- [ ] **Uses Agile SpecFirst language** - Should mention methodology and specification process
- [ ] **Guides toward SPECIFICATIONS.md** - Should talk about creating complete specifications
- [ ] **Acts as engineering partner** - Should feel like consulting with a software engineer
- [ ] **Asks about user experience** - Should inquire about workflows and user needs
- [ ] **Considers technical constraints** - Should ask about preferences and limitations

### **Red Flags (What NOT to see):**
- ❌ **Immediate code blocks** without specification discussion
- ❌ **Technology assumptions** without asking user preferences  
- ❌ **Implementation details** before requirements are clear
- ❌ **Missing specification engineering** conversation
- ❌ **Jumping to solutions** without understanding the problem

## 🔧 **If Test Fails**

### **Potential Issues:**
1. **`.cursorrules` not loaded** - Cursor might not be reading the updated rules
2. **Cache issues** - Cursor might be using cached behavior
3. **Syntax errors** - Check .cursorrules file for formatting issues
4. **File location** - Ensure .cursorrules is in the project root

### **Debugging Steps:**
1. **Check .cursorrules location** - Must be in project root directory
2. **Restart Cursor** - Close and reopen Cursor application
3. **Clear Cursor cache** - If available in settings
4. **Test in fresh project** - Create new project with .cursorrules copy
5. **Check file syntax** - Ensure no formatting errors in .cursorrules

## 📊 **Success Criteria**

### **The test is successful if:**
- ✅ Cursor immediately starts specification refinement conversation
- ✅ User feels guided through requirements discovery process  
- ✅ No code is generated until specifications are complete
- ✅ AI acts like an experienced software engineer consultant
- ✅ Process feels collaborative and supportive

### **Perfect Score Indicators:**
- User thinks "This AI really understands software engineering"
- Conversation feels like pair programming on requirements
- User learns things about their project they hadn't considered
- Specifications that result are comprehensive and clear
- User feels confident the specifications capture their vision

---

**Ready to test? Try opening a new Cursor Chat tab and use one of the test scenarios above!** 