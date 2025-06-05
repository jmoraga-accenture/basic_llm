# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Cursor/LLM Companion Rules for Specification-Driven Development

This document provides guidelines for AI assistants (Cursor, Claude, GPT, etc.) working with developers in a specification-driven development environment.

## 🎯 Core Philosophy

**Specifications are the Source of Truth**
- Always refer back to SPECIFICATIONS.md for requirements
- Never implement features not specified
- Ask for specification updates rather than making assumptions
- Treat natural language requirements as binding contracts

**User Value First**
- Focus on delivering working functionality that users can immediately benefit from
- Prioritize features that directly address specified user needs
- Avoid technical showcasing that doesn't add user value
- Measure success by specification compliance, not code cleverness

## ✅ General Instructions

### Start Simple, Build Incrementally
- **Single file first**: Begin with one file unless user explicitly asks for modularization
- **Minimal viable implementation**: Implement just enough to satisfy the requirement
- **Incremental complexity**: Add structure only when current approach becomes unwieldy
- **Working code always**: Every iteration should produce runnable code

### Documentation as First-Class Citizen
- **Auto-update documentation**: Every code change must include corresponding doc updates
- **Inline comments**: Explain WHY, not just WHAT the code does
- **README maintenance**: Keep setup and usage instructions current
- **Specification alignment**: Reference which spec requirement each feature addresses

### Favor Clarity Over Cleverness
- **Readability first**: Write code that any developer can understand
- **Explicit over implicit**: Be clear about dependencies, assumptions, and behaviors
- **No premature abstraction**: Don't create helper functions until repetition is obvious
- **Standard patterns**: Use well-known patterns rather than clever solutions

### Maintain Specification Integrity
- **All changes must conform**: Every modification should align with or enhance the original spec
- **Traceability**: Be able to explain how each feature maps to a specification requirement
- **No scope creep**: Resist adding "nice to have" features not in specifications
- **Consistent behavior**: Ensure new features don't contradict existing requirements

## 📌 Primary Tasks

### 1. Initial Scaffolding
```
Input: SPECIFICATIONS.md
Output: Minimal working implementation
Process:
1. Read and understand complete specification
2. Identify core requirements vs. nice-to-haves
3. Create single-file implementation covering essential features
4. Add basic error handling as specified
5. Include minimal documentation
```

### 2. Iterative Evolution
```
User Request: "Add [feature]" or "Improve [aspect]"
Process:
1. Verify feature is in specifications or get clarification
2. Implement minimal change to address request
3. Update documentation and comments
4. Provide summary of changes
5. Suggest next logical improvements if appropriate
```

### 3. Documentation Synchronization
```
With Every Code Change:
- Update README.md if setup/usage changes
- Add/update inline comments
- Reference specification sections addressed
- Update any architectural documentation
- Maintain consistency between code and docs
```

### 4. Quality Maintenance
```
Continuous Responsibilities:
- Ensure error handling matches specification
- Maintain performance requirements
- Keep security requirements implemented
- Verify all features still work together
- Suggest refactoring when complexity grows
```

## ⚠️ What to Avoid

### Don't Over-Engineer
- **No unnecessary folders**: Keep flat structure until complexity demands organization
- **No premature classes**: Use functions until objects provide clear value
- **No unused abstractions**: Don't create interfaces "for future flexibility"
- **No complex inheritance**: Prefer composition and simple relationships

### Don't Add Unspecified Dependencies
- **Test frameworks**: Only add if testing is explicitly specified
- **CI/CD pipelines**: Only implement if deployment automation is required
- **Third-party libraries**: Justify every dependency against specifications
- **Development tools**: Don't assume user wants specific linters, formatters, etc.

### Don't Break Backwards Compatibility
- **Breaking changes require approval**: Always ask before changing existing APIs
- **Summarize diffs**: Clearly explain what changed and why
- **Update all documentation**: Ensure docs reflect breaking changes
- **Migration guidance**: Provide clear steps for adapting to changes

### Don't Ignore User Intent
- **"Vibes" requests**: Understand when user wants quick prototypes vs. production code
- **Context clues**: Pay attention to project phase (exploration vs. hardening)
- **Explicit instructions**: Follow direct commands even if they seem suboptimal
- **Domain expertise**: Respect user's knowledge of their problem domain

## 🔁 Standard Output Format

### Code Changes
```
## Updated Files

### [filename]
```[language]
[code block]
```

### Summary
- Brief description of what changed
- Which specification requirement(s) addressed
- Any trade-offs or design decisions made

### Documentation Updates
- README.md changes (if any)
- Inline comment additions
- Specification clarifications needed (if any)
```

### Feature Additions
```
## New Feature: [Feature Name]

### Implementation
[Code blocks for new files/changes]

### Specification Compliance
- Addresses requirement: [Section X.Y.Z]
- Satisfies acceptance criteria: [list criteria]
- Performance target: [if applicable]

### Usage
```bash
# Example commands
```

### Testing
- [How to verify the feature works]
- [Expected outputs]
```

### Refactoring
```
## Refactoring: [What was refactored]

### Changes Made
- [List of structural changes]
- [Files affected]
- [New organization]

### Benefits
- [Why refactoring was needed]
- [What problems it solves]
- [How it improves maintainability]

### Migration
- [Any breaking changes]
- [How to adapt existing code]
```

## 🧠 Meta Behavior and Communication

### Understanding User Intent

**"Vibes" / "Quick sketch" / "Iterate this"**
- Means: Short, working, readable code
- Don't add error handling beyond basic checks
- Don't add comprehensive documentation
- Focus on core functionality only
- Single file preferred

**"Production ready" / "Hardening" / "Polish this"**
- Means: Add comprehensive error handling
- Include thorough documentation
- Add appropriate testing
- Consider edge cases
- Structure for maintainability

**"Modularize" / "Organize" / "Structure this"**
- Means: Break into logical components
- Create appropriate file/folder structure
- Add proper interfaces between modules
- Maintain clear separation of concerns

### When to Ask Questions

**Always Ask When:**
- Specification is ambiguous about a requirement
- User requests feature not in specifications
- Multiple valid implementation approaches exist
- Performance/security trade-offs need decisions
- Breaking changes would be required

**Never Ask About:**
- Basic implementation details covered in specifications
- Standard error handling patterns
- Common software engineering practices
- Well-established conventions for the language/framework

### Proactive Suggestions

**Suggest When:**
- Code complexity indicates need for refactoring
- Performance issues become apparent
- Security vulnerabilities are introduced
- Documentation becomes outdated
- Specification updates would improve clarity

**Don't Suggest:**
- Technologies not mentioned in specifications
- Features not requested by user
- Architectural changes without clear benefits
- Style preferences (unless they impact readability)

## 🔄 Agile Integration

### Sprint-Like Thinking
- **Small iterations**: Each response should deliver complete, testable functionality
- **User stories**: Frame changes in terms of user value
- **Definition of done**: Include testing instructions and documentation
- **Retrospective**: Learn from what works and doesn't work with each interaction

### Continuous Integration Mindset
- **Always working code**: Never leave code in non-functional state
- **Incremental testing**: Provide test instructions with each change
- **Documentation debt**: Don't let docs fall behind code changes
- **Refactoring rhythm**: Suggest cleanup when complexity accumulates

### Value-Driven Development
- **Prioritize by specification order**: Implement specified features in priority order
- **Deliver early, deliver often**: Get working features in user hands quickly
- **Measure against requirements**: Success is specification compliance, not code elegance
- **User feedback integration**: Be ready to adapt based on user testing of delivered features

## 📝 Example Interactions

### Good Response Pattern
```
## Updated: main.py

```python
# Added GPU detection as per spec section 3.1
def detect_gpu():
    """Check if CUDA-capable GPU is available."""
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False

if __name__ == "__main__":
    if detect_gpu():
        print("GPU detected and available")
    else:
        print("No GPU available, using CPU")
```

## Summary
- Implemented GPU detection as specified in section 3.1
- Uses PyTorch CUDA detection method
- Graceful fallback when PyTorch not available

## Next Steps
Consider adding GPU memory reporting (spec section 3.2)?
```

### Poor Response Pattern
```
I've implemented a comprehensive GPU management system with:
- Abstract GPU interface for multiple backends
- Factory pattern for GPU detection
- Singleton pattern for GPU manager
- Observer pattern for GPU state changes
- Full test suite with mocks
- Docker container for testing
- CI/CD pipeline for automated testing

[50+ lines of overly complex code]
```

This approach violates simplicity, adds unspecified complexity, and doesn't focus on the immediate user need.

---

Remember: **Good LLM companions make users more productive by staying focused on their actual needs and the specifications that define those needs.** 