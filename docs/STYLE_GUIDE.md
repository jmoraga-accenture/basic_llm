# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Code Style Guide

This document outlines the coding standards and best practices for the Basic OpenAI API Client project.

## File Organization

### Copyright Notice
Every source file must begin with the copyright notice:
```python
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
```

### File Headers
- Copyright notice
- Module docstring
- Imports (standard library, third-party, local)
- Constants
- Classes
- Functions
- Main execution block (if applicable)

## Code Style

### General Rules
- Maximum line length: 80 characters
- Use 4 spaces for indentation
- No tabs
- No trailing whitespace
- Files end with a single newline
- Use UTF-8 encoding

### Naming Conventions
- Classes: `CamelCase`
- Functions and variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_single_leading_underscore`
- Protected members: `_single_leading_underscore`
- Module names: `snake_case`
- Package names: `snake_case`

### Imports
Order imports in the following groups:
1. Standard library imports
2. Third-party imports
3. Local application imports

Separate each group with a blank line.

### Docstrings
Use Google style docstrings:

```python
def function_name(param1: type, param2: type) -> return_type:
    """Short description.

    Longer description if needed.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of return value.

    Raises:
        ExceptionType: Description of when this exception is raised.
    """
```

### Type Hints
- Use type hints for all function parameters and return values
- Use `typing` module for complex types
- Include type hints in class attributes
- Document type hints in docstrings

### Error Handling
- Use specific exception types
- Include meaningful error messages
- Clean up resources in finally blocks
- Log errors appropriately
- Handle exceptions at the appropriate level

### Testing
- Write unit tests for all functions
- Include integration tests
- Test edge cases
- Test error conditions
- Maintain test coverage
- Use descriptive test names

### Documentation
- Keep documentation up to date
- Document all public APIs
- Include usage examples
- Document exceptions
- Document side effects
- Keep comments relevant

### Performance
- Profile code when necessary
- Optimize critical paths
- Use appropriate data structures
- Consider memory usage
- Handle resources efficiently
- Use async operations when appropriate

### Security
- Never hardcode credentials
- Use environment variables
- Validate input data
- Handle sensitive data securely
- Follow security best practices
- Keep dependencies updated

## Tools

### Linting
Use the following tools:
- pylint
- flake8
- mypy
- black
- isort

### IDE Configuration
Configure your IDE to:
- Use 4 spaces for indentation
- Remove trailing whitespace
- Insert final newline
- Use UTF-8 encoding
- Enable type checking
- Enable linting

## Best Practices

### Code Organization
- Follow single responsibility principle
- Keep functions small and focused
- Use meaningful names
- Write self-documenting code
- Avoid code duplication
- Use appropriate design patterns

### Version Control
- Write meaningful commit messages
- Keep commits focused
- Use feature branches
- Review code before committing
- Keep the history clean
- Follow Git flow

### Documentation
- Keep README up to date
- Document all changes
- Include setup instructions
- Document dependencies
- Include usage examples
- Keep documentation in sync with code

## License

Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

All rights reserved. 