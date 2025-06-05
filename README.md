# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst: AI-Native Intentional Software Development Framework

*Specification-Driven Development for the LLM Era*

A framework for creating software projects from natural language specifications using AI-assisted development. This project demonstrates best practices for translating user requirements into production-ready code while maintaining high standards for architecture, testing, and documentation.

## Project Philosophy

This framework embodies the principle that **clear specifications lead to better software**. Through practical application across multiple projects, we've proven that comprehensive, natural language requirements enable:

- **Universal Understanding**: All stakeholders can understand what needs to be built
- **AI-Powered Development**: LLMs can recreate entire projects from specifications alone
- **Technology Agnostic Design**: Same specs work across different programming languages and stacks
- **Iterative Refinement**: Specifications evolve independently of implementation details
- **Version Strategy Evolution**: v1 for reference implementation, v2+ for specifications only
- **Knowledge Preservation**: Patterns and preferences captured in .cursorrules for consistency

## Framework Structure

```
.
├── README.md                     # This file - Framework overview
├── .cursorrules                  # Development framework + user preferences
├── docs/
│   ├── STYLE_GUIDE.md           # Code quality standards
│   ├── BEST_PRACTICES.md        # Development guidelines
│   ├── CURSOR_LLM_RULES.md      # AI assistant behavioral guidelines
│   └── USER_PREFERENCES_SUMMARY.md # User-specific patterns and defaults
├── v1/                          # Reference implementation (Python OpenAI client)
│   ├── README.md                # Implementation-specific guide
│   ├── main.py                  # Main application script
│   ├── test_gpu.py              # GPU testing script
│   ├── environment.yml          # Conda environment configuration
│   ├── requirements.txt         # Python dependencies
│   ├── src/                     # Source code modules
│   ├── tests/                   # Unit and integration tests
│   └── config/                  # Configuration templates
├── v2/
│   └── SPECIFICATIONS.md        # Web-based AI testing application specs
└── v3/
    └── SPECIFICATIONS.md        # OpenAI-powered HOI4 script generator specs
```

## How to Use This Framework

### For Users (Specification Writers)

1. **Define Requirements Clearly**
   - Write in natural language that any stakeholder can understand
   - Focus on WHAT the system should do, not HOW to implement it
   - Include user experience requirements and acceptance criteria
   - Specify performance requirements and constraints
   - Define security and compliance requirements

2. **Follow the Specification Template**
   ```
   - Project Overview
   - Core Requirements (by functional area)
   - System Architecture (high-level)
   - User Experience Requirements
   - Performance Criteria
   - Security Requirements
   - Testing Requirements
   ```

3. **Best Practices for Users**
   - Use concrete examples and scenarios
   - Define success criteria for each requirement
   - Include error handling expectations
   - Specify data formats and interfaces
   - Consider edge cases and failure modes
   - Write for your target audience's technical level

### For Developers and LLMs (Implementation)

1. **Read Specifications Thoroughly**
   - Understand the complete requirements before coding
   - Identify technical decisions not specified by requirements
   - Plan architecture based on specified constraints
   - Choose appropriate technology stack for requirements

2. **Follow Implementation Rules**
   - Implement ALL specified requirements
   - Add comprehensive error handling
   - Include thorough testing (unit, integration, performance)
   - Follow language-specific style guides
   - Document implementation decisions not in specifications
   - Add copyright notices and proper licensing

3. **Quality Standards**
   - Code should be production-ready, not proof-of-concept
   - Include proper dependency management
   - Implement security best practices
   - Provide clear setup and usage instructions
   - Include troubleshooting documentation

### For AI/LLM Code Generation

1. **Specification Compliance**
   - Generate code that fulfills ALL requirements in SPECIFICATIONS.md
   - Follow the STYLE_GUIDE.md for the chosen language
   - Implement proper error handling for all specified scenarios
   - Include comprehensive testing as specified
   - **Read .cursorrules for user-specific preferences and patterns**

2. **Code Quality Requirements**
   - Generate production-ready code with proper structure
   - Include type hints/annotations where language supports them
   - Add comprehensive docstrings/comments
   - Implement proper dependency management
   - Follow security best practices (no hardcoded secrets, etc.)
   - **Use absolute paths in terminal commands to avoid confusion**

3. **Project Structure Requirements**
   - Create appropriate directory structure for the language
   - Include configuration management with templates
   - Set up testing framework with primary test case verification
   - Provide clear documentation and troubleshooting guides
   - Include setup/installation instructions for multiple environments
   - **Test the primary use case to ensure specifications are met**

## Framework Evolution and Lessons Learned

### Key Insights from Project Development

**Specification Completeness Test**: The ultimate test of specification quality is whether another LLM can recreate the entire project from the specs alone. Our v2 and v3 projects proved this approach works.

**Version Strategy Optimization**: 
- **v1**: Complete implementation committed (reference baseline)
- **v2+**: Only SPECIFICATIONS.md committed (implementations are regeneratable)
- **Result**: Dramatically reduced repository size while maintaining full functionality

**AI Integration Patterns**:
- **Structured Prompts**: Comprehensive system prompts with domain-specific knowledge
- **Guardrails**: Validation rules ensure correct output format and syntax
- **Error Handling**: Graceful API failure handling with user-friendly messages
- **Configuration Management**: Secure credential handling with templates

**Environment Management Lessons**:
- **Multi-Package Manager Support**: Document pip, conda, and mamba installation paths
- **Hardware Considerations**: CUDA detection, GPU fallback scenarios, memory optimization
- **Diagnostic Commands**: Verification steps with expected outputs
- **Common Issues**: Document frequent environment conflicts and resolutions

**User Experience Patterns**:
- **Primary Test Case**: Always implement and verify the main specification requirement
- **Real-World Focus**: Production-ready applications, not demos or prototypes
- **Incremental Development**: Working functionality at each phase
- **Complete Solutions**: End-to-end implementations, not partial features

### Framework Components

**Core Files**:
- **.cursorrules**: Development framework rules + user-specific preferences
- **README.md**: Framework overview and usage guidelines
- **docs/**: Comprehensive development guides and patterns

**Quality Assurance**:
- **Primary test cases**: Verify main requirements work perfectly
- **Documentation testing**: Setup instructions validated on fresh environments
- **Cross-platform support**: Multiple OS and package manager compatibility
- **Security validation**: Credential protection and .gitignore effectiveness

## Language-Specific Guidelines

### Python Projects
- Follow PEP 8 and Google Python Style Guide
- Use type hints throughout
- Include requirements.txt and/or pyproject.toml
- Use pytest for testing with coverage reporting
- Include pre-commit hooks for code quality
- Use virtual environments (venv, conda, etc.)

### JavaScript/Node.js Projects
- Follow ESLint and Prettier configurations
- Use TypeScript for type safety
- Include package.json with proper scripts
- Use Jest or similar for testing
- Include proper error handling and logging
- Use npm/yarn for dependency management

### Go Projects
- Follow official Go style guidelines
- Use go.mod for dependency management
- Include proper package structure
- Use built-in testing framework
- Include proper error handling
- Use gofmt and golint

### Rust Projects
- Follow official Rust style guidelines
- Use Cargo for dependency management
- Include proper crate structure
- Use built-in testing framework
- Handle Result types properly
- Use clippy for additional linting

### Java Projects
- Follow Google Java Style Guide
- Use Maven or Gradle for dependency management
- Include proper package structure
- Use JUnit for testing
- Include proper exception handling
- Use static analysis tools (SpotBugs, etc.)

## Architecture Principles

### Modular Design
- Separate concerns into distinct modules/packages
- Define clear interfaces between components
- Support dependency injection where appropriate
- Enable easy testing and mocking

### Configuration Management
- Externalize all configuration
- Support environment-specific settings
- Never hardcode secrets or sensitive data
- Provide sensible defaults with override capability

### Error Handling
- Handle all error conditions gracefully
- Provide meaningful error messages
- Log errors appropriately
- Include recovery mechanisms where possible

### Testing Strategy
- Unit tests for all business logic
- Integration tests for component interactions
- Performance tests for critical paths
- Security tests for sensitive operations

## Version History

- **v1**: Python implementation of OpenAI API client with GPU testing
  - Demonstrates modular architecture with proper separation of concerns
  - Includes comprehensive testing framework with pytest
  - Shows proper configuration management and secure credential handling
  - Implements security best practices with config templates
  - Features: OpenAI API client, GPU detection, neural network testing, CUDA verification

- **v2**: Specification-only web-based AI testing application
  - Demonstrates pure specification-driven development approach
  - Complete project definition in SPECIFICATIONS.md only
  - Shows technology-agnostic requirement writing
  - Features: OpenAI model testing, neural network architecture testing, web interface
  - **Note**: Implementation generated from specifications, not committed to repository

- **v3**: OpenAI-powered Hearts of Iron IV script generator
  - Advanced AI integration with structured prompts and guardrails
  - Domain-specific code generation with comprehensive HOI4 knowledge
  - Demonstrates AI instruction frameworks for specialized tasks
  - Features: Natural language to HOI4 code generation, OpenAI GPT-4o integration, web interface
  - **Note**: Implementation generated from specifications, not committed to repository

## Contributing

1. **Adding New Versions**
   - Create new version directory (v2, v3, etc.)
   - Implement same SPECIFICATIONS.md in different language/approach
   - Include version-specific README with implementation notes
   - Update this framework README with new version info

2. **Improving Specifications**
   - Enhance clarity and completeness
   - Add new requirement categories
   - Include more detailed examples
   - Improve user experience descriptions

3. **Updating Guidelines**
   - Add support for new programming languages
   - Update style guides and best practices
   - Include new architectural patterns
   - Add security and performance guidance

## License

Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

All rights reserved.

This framework is designed to demonstrate specification-driven development practices and may be used for educational and research purposes.