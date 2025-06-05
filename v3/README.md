# Hearts of Iron IV Script Generator - v3

## Overview

A Flask web application that uses **OpenAI GPT-4o** to generate Hearts of Iron IV scripting code from natural language requests. Simply describe what you want to achieve in HOI4, and get professionally crafted, syntactically correct scripting code!

## Features

- **🤖 AI-Powered Generation**: Uses OpenAI GPT-4o for intelligent code creation
- **🧠 HOI4 Expert Knowledge**: Comprehensive HOI4 scripting guidelines and guardrails
- **📝 Natural Language Processing**: Describe your needs in plain English
- **🎯 Multiple Script Types**: Supports decisions, events, national focuses, modifiers, and more
- **✅ Syntax Validation**: Generates syntactically correct HOI4 code
- **📋 Copy-to-Clipboard**: Easy code copying functionality
- **💡 Examples Library**: Built-in examples to get you started
- **🎨 Modern UI**: Clean, responsive web interface
- **⚡ Real-time Generation**: Instant AI-powered code generation

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key

```bash
# Copy the template and add your API key
cp config/config.json.template config/config.json
# Edit config/config.json and add your OpenAI API key
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

Navigate to: http://localhost:5000

## Primary Test Case

The main test case demonstrates land productivity enhancement:

**Request**: "Create code to increment all the user's land productivity by 10%"

**Generated Output**:
- Decision system for productivity boost
- Dynamic modifier for state-level effects  
- Localization entries for UI text
- Complete HOI4-ready code structure

## Supported Request Types

### Economic/Production
- **Keywords**: "productivity", "efficiency", "land", "territory", "state"
- **Example**: "Increase all state productivity by 15%"
- **Generates**: Decision with dynamic modifiers

### Political Power
- **Keywords**: "political power", "pp", "politics"
- **Example**: "Create an event that gives 100 political power"
- **Generates**: Country event with PP reward

### Technology/Research
- **Keywords**: "technology", "tech", "research", "unlock"
- **Example**: "Make a focus that unlocks tank technology"
- **Generates**: National focus with tech bonuses

### Diplomacy
- **Keywords**: "relations", "diplomatic", "neighbors"
- **Example**: "Improve relations with all neighbors by 25"
- **Generates**: Decision with diplomatic effects

### National Ideas
- **Keywords**: "national spirit", "idea", "factory output"
- **Example**: "Create a spirit that increases factory output by 20%"
- **Generates**: Decision + modifier for industrial bonuses

### War Events
- **Keywords**: "war", "declare", "trigger"
- **Example**: "Event when Germany declares war on Poland"
- **Generates**: Triggered country event

## Code Structure

```
v3/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface
├── requirements.txt      # Python dependencies
├── .gitignore           # Git exclusions
└── README.md            # This file
```

## Generated Code Format

All generated code follows HOI4 modding standards:

- **File Paths**: Proper game directory structure
- **Syntax**: Valid HOI4 scripting syntax
- **Comments**: Explanatory comments included
- **Localization**: English localization entries
- **Modifiers**: Properly balanced effect values

## Usage Examples

### Example 1: Economic Boost
```
Request: "Create code to increment all the user's land productivity by 10%"
Output: Decision + modifier + localization for state productivity
```

### Example 2: Political Event
```
Request: "Create an event that gives the player 100 political power"
Output: Country event with political power reward
```

### Example 3: Technology Focus
```
Request: "Make a national focus that unlocks advanced tank technology"
Output: Focus tree entry with technology bonuses
```

## Technical Details

- **Framework**: Flask 2.3.3
- **AI Engine**: OpenAI GPT-4o for intelligent code generation
- **API Integration**: OpenAI Python client with structured prompts
- **HOI4 Knowledge**: Comprehensive scripting syntax and best practices
- **Guardrails**: AI instructions ensure valid, syntactically correct code
- **Configuration**: JSON-based API key management

## Error Handling

- Input validation for empty requests
- Graceful fallback for unmatched patterns
- User-friendly error messages
- Suggestion system for improvements

## Development

### Adding New Patterns

1. Update `_setup_patterns()` method in `HOI4ScriptGenerator`
2. Add corresponding generator method
3. Create appropriate templates
4. Test with example requests

### Template Customization

Templates are stored in the `_load_templates()` method and use Jinja2 syntax for variable substitution.

## Browser Compatibility

- Modern browsers with ES6+ support
- Chrome 60+, Firefox 55+, Safari 11+, Edge 79+
- JavaScript required for functionality

## Troubleshooting

### Common Issues

1. **Server won't start**
   - Check Python version (3.7+)
   - Verify Flask installation
   - Check port 5000 availability

2. **Code generation errors**
   - Try rephrasing your request
   - Use keywords from supported categories
   - Check example requests for format

3. **Copy functionality not working**
   - Ensure HTTPS or localhost context
   - Modern browser required for clipboard API

## Contributing

This project follows specification-driven development. To contribute:

1. Update SPECIFICATIONS.md first
2. Implement changes based on specifications
3. Test all supported request types
4. Verify HOI4 code validity

## License

Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

---

**Note**: This application generates template HOI4 code. Always test generated scripts in a development environment before using in your main game saves. 