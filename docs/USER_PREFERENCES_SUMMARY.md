# User Preferences Summary - Jaime Moraga

This document summarizes the key development preferences and patterns observed through extensive AI assistant collaboration.

## 🎯 Core Development Philosophy

### Specification-Driven Development
- **Always start with comprehensive specifications** before any coding
- Specifications must be **technology-agnostic** and readable by any developer
- Specs should be **complete enough for LLM regeneration** of entire projects
- **v1/ for reference implementations, v2+ only SPECIFICATIONS.md**

### Quality and Security First
- **Production-ready code** from the start, not demos or prototypes
- **Security-conscious development** with proper credential management
- **Comprehensive error handling** with user-friendly messages
- **Cross-platform compatibility** consideration from day one

## 🛠️ Technical Preferences

### Python Development
- **Environment**: mamba/conda preferred over pip
- **Code Style**: PEP 8, comprehensive type hints, Google-style docstrings
- **Copyright**: Always include "# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)"
- **Testing**: Primary test case verification with real user workflow testing

### AI Integration
- **When using AI APIs**: Provide comprehensive system prompts with guardrails
- **OpenAI Integration**: Structure prompts with syntax rules, examples, and validation
- **Error Handling**: Graceful API failure handling with fallback mechanisms

### Web Development
- **Framework**: Flask for simplicity and minimal overhead
- **Architecture**: Single-page applications with modern responsive UI
- **Security**: Config templates, proper .gitignore, no hardcoded secrets

## 📁 Project Structure Patterns

```
project_root/
├── .cursorrules              # Development framework + user preferences
├── SPECIFICATIONS.md         # Complete, technology-agnostic specs
├── README.md                # Comprehensive setup and usage guide
├── .gitignore               # Comprehensive security exclusions
├── config/
│   ├── config.json.template # Template for sensitive configurations
│   └── config.json          # Actual config (git-ignored)
├── v1/                      # Reference implementation (commit all)
│   ├── app.py              # Main application
│   ├── requirements.txt    # Dependencies
│   └── test_primary_case.py # Verification script
└── v2+/                     # Future versions (SPECIFICATIONS.md only)
    └── SPECIFICATIONS.md    # Complete project definition
```

## 🎨 Communication & Interaction Style

### AI Assistant Expectations
- **Ask questions rather than make assumptions** about unclear requirements
- **Use absolute paths** in terminal commands
- **Implement complete solutions** end-to-end, not partial features
- **Validate generated code** against original specifications
- **Preserve conversation context** and reference previous decisions

### Feedback Style
- **Visual indicators**: ✅❌🎯🚀 for status and progress
- **Technical precision**: Specific versions, configurations, and details
- **Educational value**: Explain "why" behind technical decisions
- **Problem-solution format**: Clear identification followed by actionable steps

## 🔧 Environment-Specific Considerations

### Development Environment
- **OS**: WSL2/Ubuntu development environment
- **Hardware**: NVIDIA GPU with CUDA support awareness
- **IDE**: VS Code with proper Python interpreter configuration
- **Package Management**: mamba > conda > pip preference order

### Dependency Management
- **Multi-manager support**: Document pip, conda, and mamba paths
- **CUDA considerations**: PyTorch build string verification
- **Environment verification**: Diagnostic commands and expected outputs
- **Troubleshooting**: Common conflicts and resolution steps

## 📊 Quality Assurance Patterns

### Testing Strategy
- **Primary test cases**: Always implement and verify main requirements
- **User workflow testing**: Complete end-to-end user journey validation
- **Edge case handling**: Comprehensive error scenarios and graceful degradation
- **Documentation testing**: Verify setup instructions work for new users

### Decision-Making Criteria
- **Simplicity first**: Choose simpler solutions when functionality is equivalent
- **Future-proofing**: Design for extensibility and maintainability
- **User-centric**: Prioritize end-user experience over developer convenience
- **Evidence-based**: Prefer tested patterns over experimental approaches

## 🚀 Notable Patterns from Recent Projects

### V2 AI Testing Web App
- Flask + OpenAI integration with structured prompts
- CUDA environment troubleshooting and verification
- Multi-package manager support documentation
- Real-time neural network testing with GPU fallback

### V3 HOI4 Script Generator
- OpenAI GPT-4o with comprehensive domain-specific instructions
- Guardrails for syntactically correct game scripting code
- Configuration management for API keys
- Primary test case: "land productivity boost" verification

## 💡 Key Insights for Future AI Assistants

1. **Always read existing SPECIFICATIONS.md** before starting any implementation
2. **Question specification completeness** - can another LLM recreate this from specs alone?
3. **Security is non-negotiable** - proper credential handling, comprehensive .gitignore
4. **Documentation is a core deliverable** - comprehensive README, setup guides, troubleshooting
5. **Test the primary use case** - verify the main requirement works perfectly
6. **Use absolute paths** in terminal operations to avoid directory confusion
7. **Framework thinking** - build reusable patterns, not one-off solutions
8. **Real-world focus** - production-ready code that users can actually deploy

---

**Last Updated**: Based on conversation through v3 HOI4 Script Generator project
**Context**: Specification-driven development framework with OpenAI integration patterns 