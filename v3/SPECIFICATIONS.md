# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Project Specifications - v3: Hearts of Iron IV Script Generator

This document describes the requirements for a web-based Hearts of Iron IV (HOI4) scripting code generator that allows users to input natural language requests and receive properly formatted HOI4 scripting code.

## Project Overview

Create a local web application that provides an interface for generating Hearts of Iron IV scripting code based on user descriptions. Users should be able to describe what they want to achieve in HOI4 and receive accurate, properly formatted scripting code that can be directly used in their HOI4 modifications.

The application serves as a bridge between natural language descriptions and HOI4's complex scripting syntax, making modding more accessible to users who understand the game mechanics but struggle with the scripting syntax.

## Core Requirements

### 1. Web Application Infrastructure

**Purpose**: Provide a local web server with browser-based interface for HOI4 script generation

**Requirements**:
- Run locally on user's machine
- Accessible through web browser (localhost)
- Single-page application with clean, intuitive interface
- Real-time code generation with immediate feedback
- Syntax highlighting for generated HOI4 code
- Copy-to-clipboard functionality for generated code
- Error handling with user-friendly messages

**Expected Behavior**:
- Application starts with a simple command
- User can navigate to localhost URL to access interface
- All functionality accessible through web browser
- No command-line interaction required for code generation
- Graceful handling of invalid requests and generation errors

### 2. HOI4 Script Code Generation

**Purpose**: Generate accurate HOI4 scripting code based on natural language requests

**Requirements**:
- Text input area for natural language requests
- Code generation button to process requests
- Display generated HOI4 code with proper syntax highlighting
- Support for common HOI4 scripting patterns and syntax
- Generate code for various HOI4 modding scenarios
- Provide code comments explaining the generated script
- Handle multiple types of HOI4 scripting (events, decisions, focuses, etc.)

**User Workflow**:
1. User enters natural language description of desired HOI4 functionality
2. User clicks generate button to process request
3. Application analyzes the request and generates appropriate HOI4 code
4. Application displays formatted code with syntax highlighting
5. User can copy the generated code for use in their HOI4 mod
6. User can submit additional requests or modify existing ones

**Expected Code Generation Capabilities**:
- National decisions and decision categories
- National focus trees and individual focuses
- Events (country events, news events, etc.)
- Ideas and national spirits
- Technologies and doctrines
- Country modifiers and state modifiers
- Economic and political actions
- Military and industrial commands

### 3. HOI4 Scripting Knowledge Base

**Purpose**: Provide accurate HOI4 scripting syntax and patterns

**Requirements**:
- Built-in knowledge of HOI4 scripting syntax
- Understanding of common HOI4 modding patterns
- Proper variable names and scope handling
- Correct trigger and effect syntax
- Appropriate localization key generation
- Valid country tags and state IDs when applicable
- Proper file structure suggestions

**Expected Behavior**:
- Generate syntactically correct HOI4 code
- Use appropriate scopes for different script types
- Include proper localization keys with descriptive names
- Suggest appropriate file names and locations
- Provide explanatory comments within generated code
- Handle edge cases and common scripting pitfalls

## User Experience Requirements

### Interface Layout
- Clean, modern single-page design
- Prominent text area for user input
- Clear "Generate Code" button
- Large code display area with syntax highlighting
- Copy button for easy code extraction
- Request history or examples section

### Results Display
- Generated code displayed in formatted code block
- Syntax highlighting appropriate for HOI4 scripting
- Line numbers for easy reference
- Explanatory comments included in generated code
- File location suggestions displayed above code
- Copy-to-clipboard functionality with visual feedback

### User Interaction Flow
- Users can enter requests in natural language
- Generation happens on-demand with button click
- Multiple requests can be processed in sequence
- Clear visual feedback during code generation process
- No page refresh required between requests

## Technical Requirements

### OpenAI API Integration
- Use OpenAI GPT-4o for intelligent HOI4 code generation
- API key configuration from /config/config.json
- Structured prompts with comprehensive HOI4 scripting guidelines
- Context-aware generation based on natural language requests
- Proper error handling for API failures and rate limits
- Fallback mechanisms for connectivity issues

### AI Instruction System
- Comprehensive system prompt with HOI4 syntax rules and examples
- Guardrails to ensure valid, syntactically correct HOI4 code output
- Context injection for different script types (decisions, events, focuses)
- Parameter extraction and validation within AI prompts
- Output format specifications for consistent code structure
- Example-driven prompts showing proper HOI4 patterns

### HOI4 Knowledge Integration
- AI prompt contains complete HOI4 scripting syntax reference
- Common triggers, effects, and scopes documentation in prompts
- File structure and organization guidelines for AI
- Proper localization key generation patterns
- Modding best practices and conventions for AI to follow
- Version compatibility considerations in AI instructions

## AI Instruction Framework

### System Prompt Requirements
The AI system must receive comprehensive instructions containing:

**HOI4 Syntax Rules**:
- Complete HOI4 scripting syntax with examples
- Proper scope usage (country, state, character, etc.)
- Trigger and effect syntax patterns
- Localization key formatting rules
- File naming and organization conventions

**Code Generation Guardrails**:
- Always include file path comments (# File: path/to/file.txt)
- Generate syntactically valid HOI4 code only
- Include explanatory comments for complex logic
- Use proper indentation and formatting
- Generate localization entries when needed
- Follow HOI4 modding best practices

**Output Format Specifications**:
- Start with file path comment
- Include complete code blocks with proper syntax
- Add explanatory comments throughout
- End with localization if applicable
- Use consistent naming conventions
- Provide installation/usage notes when relevant

### Example AI Instructions (Subset)
```
You are a Hearts of Iron IV (HOI4) scripting expert. Generate valid HOI4 mod code based on user requests.

CRITICAL RULES:
1. Always start with file path: # File: path/to/file.txt
2. Use valid HOI4 syntax only
3. Include explanatory comments
4. Generate localization when needed
5. Follow proper scope usage

COMMON PATTERNS:
- Decisions: Use decision categories, proper effects, costs
- Events: Include triggers, options, effects
- Focuses: Use prerequisites, completion rewards, costs
- Modifiers: Proper effect values, meaningful names

EXAMPLE DECISION STRUCTURE:
# File: common/decisions/example_category.txt
example_category = {
    example_decision = {
        icon = generic_political_discourse
        available = { # conditions }
        cost = 50
        complete_effect = { # effects }
    }
}
```

## Test Cases and Examples

### Primary Test Case: Land Productivity Increase
**User Request**: "Create code to increment all the user's land productivity by 10%"

**Expected Generated Code**:
```hoi4
# File: common/decisions/productivity_boost.txt

productivity_category = {
    productivity_boost_decision = {
        icon = generic_industry
        
        available = {
            # Available to any country
        }
        
        visible = {
            # Always visible
        }
        
        cost = 50  # Political power cost
        
        ai_will_do = {
            factor = 1
        }
        
        complete_effect = {
            # Increase productivity in all owned states by 10%
            every_owned_state = {
                add_building_construction = {
                    type = industrial_complex
                    level = 1
                    instant_build = yes
                }
                # Alternative: Direct productivity modifier
                add_dynamic_modifier = {
                    modifier = state_production_efficiency_boost
                    days = -1  # Permanent
                }
            }
        }
    }
}

# File: common/modifiers/productivity_modifiers.txt
state_production_efficiency_boost = {
    local_building_slots_factor = 0.1
    production_efficiency_cap_factor = 0.1
    industrial_capacity_factory = 0.1
}

# Localization file: localisation/english/productivity_decisions_l_english.yml
productivity_boost_decision:0 "Boost Land Productivity"
productivity_boost_decision_desc:0 "Increase the productivity of all our controlled territories by 10%."
```

### Additional Test Cases

**User Request**: "Create an event that gives the player 100 political power"
**User Request**: "Make a national focus that unlocks advanced tank technology"
**User Request**: "Create a decision to improve relations with all neighbors by 25"
**User Request**: "Generate code for a national spirit that increases factory output by 15%"
**User Request**: "Create an event that triggers when Germany declares war on Poland"

## Performance Criteria

### Response Times
- Code generation should complete within 10 seconds for standard requests
- Complex requests should complete within 30 seconds
- Web interface should be responsive (page loads < 3 seconds)
- Real-time feedback for generation progress

### Code Quality
- Generated code should be syntactically correct for HOI4
- Code should follow HOI4 modding best practices
- Include appropriate comments and documentation
- Use meaningful variable and localization key names

## Security Requirements

### Input Validation
- Sanitize all user input to prevent injection attacks
- Validate request length and complexity
- Handle malformed or nonsensical requests gracefully
- No execution of user-provided code on server

### Web Security
- Basic protection against common web vulnerabilities
- Safe handling of user input and generated output
- No exposure of server internals in error messages
- Secure local-only access (no external network exposure)

## Installation and Setup Requirements

### Environment Setup
- Simple installation process (single command preferred)
- Clear documentation for dependencies
- Cross-platform compatibility (Windows, macOS, Linux)
- OpenAI API key configuration required

### Configuration
- OpenAI API key configuration in /config/config.json
- Clear setup instructions for API key configuration
- Error handling for missing or invalid API keys
- Internet connection required for OpenAI API calls
- Clear error messages for configuration and connectivity issues

### Startup Process
- Single command to start the web server
- Clear indication when server is ready
- Automatic browser opening (optional)
- Graceful shutdown capability

## Development Framework Requirements

### Web Framework
- Use Flask for maximum simplicity and minimal overhead
- Single Python file application preferred for initial implementation
- Built-in template engine for code generation
- No database requirements
- No external API calls required

### Project Structure
```
v3/
├── app.py                    # Main Flask application
├── templates/
│   └── index.html           # Main web interface
├── static/
│   ├── css/                 # Styling for syntax highlighting
│   └── js/                  # Client-side functionality
├── hoi4_templates/          # HOI4 code templates
│   ├── decisions/           # Decision templates
│   ├── events/              # Event templates
│   ├── focuses/             # Focus templates
│   └── modifiers/           # Modifier templates
├── requirements.txt         # Python dependencies
├── .gitignore              # Standard exclusions
└── README.md               # Setup and usage instructions
```

### Dependencies
- Flask (web framework)
- OpenAI Python library (for GPT-4o API calls)
- Requests (for HTTP handling)
- Basic HTML/CSS/JavaScript for frontend
- Configuration management for API keys

## Implementation Priorities

### Phase 1: Basic Infrastructure
1. Flask application setup
2. Basic HTML interface
3. Simple text input and output
4. Basic code generation framework

### Phase 2: Core HOI4 Generation
1. Template system for common HOI4 patterns
2. Natural language parsing for basic requests
3. Decision and modifier generation
4. Syntax highlighting implementation

### Phase 3: Advanced Features
1. Multiple script type support (events, focuses, etc.)
2. Advanced parameter extraction
3. Code validation and error checking
4. Enhanced user interface with examples

### Phase 4: Polish and Optimization
1. Comprehensive test case coverage
2. Performance optimization
3. User experience improvements
4. Documentation and help system

## Success Criteria

### Functional Requirements
- Successfully generate code for the primary test case (land productivity increase)
- Handle at least 5 different types of HOI4 scripting requests
- Produce syntactically correct HOI4 code for all supported patterns
- Provide clear, helpful error messages for unsupported requests

### User Experience Requirements
- Intuitive interface that requires no training or documentation
- Fast response times for all standard requests
- Clean, readable generated code with helpful comments
- Easy copy-paste workflow for generated code

### Technical Requirements
- Stable local web server with no crashes
- Proper error handling for all edge cases
- Cross-platform compatibility verified
- Clean, maintainable codebase following project standards

This specification is complete and ready for implementation using our specification-driven development framework. 