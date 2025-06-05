# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Best Practices for Specification-Driven Development

This document outlines best practices for writing effective specifications and implementing them across different programming languages and technology stacks.

## Writing Effective Specifications

### 1. Start with User Needs

**Focus on Outcomes, Not Implementation**
- Describe what users need to accomplish
- Define success criteria from user perspective
- Include user workflows and scenarios
- Specify measurable acceptance criteria

**Example - Good Specification:**
> "Users must be able to test their GPU performance and receive a report showing available memory, compute capability, and benchmark results within 10 seconds."

**Example - Poor Specification:**
> "Implement CUDA calls to query GPU properties and run matrix multiplication."

### 2. Structure Requirements Clearly

**Use Consistent Organization**
```
1. Project Overview
2. Core Requirements (by functional area)
3. System Architecture (high-level)
4. User Experience Requirements  
5. Performance Criteria
6. Security Requirements
7. Testing Requirements
8. Installation and Setup Requirements
```

**Write Self-Contained Sections**
- Each section should be understandable independently
- Include cross-references where needed
- Define domain-specific terms
- Provide context for technical decisions

### 3. Be Specific About Behavior

**Define Expected Outputs**
```
Good: "Display GPU memory in GB with one decimal place (e.g., '8.5 GB')"
Poor: "Show GPU memory information"
```

**Specify Error Conditions**
```
Good: "When no GPU is available, display 'No CUDA-capable GPUs found' and continue with CPU-only mode"
Poor: "Handle GPU detection errors"
```

**Include Performance Requirements**
```
Good: "API responses must complete within 30 seconds or timeout with user-friendly error message"
Poor: "Make API calls fast"
```

### 4. Address Edge Cases

**Consider Failure Modes**
- Network connectivity issues
- Missing dependencies
- Invalid configuration
- Resource constraints
- Permission problems

**Define Graceful Degradation**
- What happens when optional features fail?
- How should the system behave with limited resources?
- What are the minimum requirements for basic functionality?

## Implementation Best Practices

### 1. Code Organization Principles

**Separation of Concerns**
- Configuration management in dedicated module
- API interactions in client layer
- Business logic separated from I/O operations
- Testing utilities in separate modules

**Dependency Management**
- Explicit dependency declarations
- Version pinning for reproducible builds
- Minimal dependency footprint
- Clear documentation of why each dependency is needed

**Error Handling Strategy**
- Fail fast for configuration errors
- Graceful degradation for optional features
- User-friendly error messages
- Appropriate logging levels

### 2. Testing Strategy

**Test Pyramid Implementation**
- Unit tests: Test individual functions/methods
- Integration tests: Test component interactions
- End-to-end tests: Test complete user workflows
- Performance tests: Verify timing requirements

**Test Coverage Guidelines**
- All public APIs must have unit tests
- All error conditions must be tested
- Performance requirements must be verified
- Configuration validation must be tested

**Mocking Strategy**
- Mock external dependencies (APIs, hardware)
- Use dependency injection for testability
- Test both success and failure scenarios
- Verify error handling paths

### 3. Security Implementation

**Credential Management**
- Never commit secrets to version control
- Use environment variables or secure config files
- Provide clear setup instructions for credentials
- Validate credentials before use

**Input Validation**
- Validate all configuration parameters
- Sanitize user inputs
- Check file permissions and paths
- Validate API responses

**Error Information Disclosure**
- Don't expose internal system details in error messages
- Log sensitive errors securely
- Provide helpful but safe error messages to users
- Use structured logging for debugging

### 4. AI API Integration Patterns

**OpenAI Integration Best Practices**
- Use structured system prompts with comprehensive domain knowledge
- Implement guardrails to ensure valid output format
- Handle rate limiting and authentication errors gracefully
- Provide fallback mechanisms for API failures
- Include token usage monitoring for cost management

**System Prompt Design**
```python
system_prompt = """You are a [domain] expert. Generate [output type] based on user requests.

CRITICAL RULES:
1. Always start with [format requirement]
2. Generate ONLY valid [syntax/format]
3. Include explanatory comments
4. Follow [domain-specific guidelines]

[Domain-specific knowledge and examples]

OUTPUT FORMAT:
[Detailed format specifications]
"""
```

**Error Handling for AI APIs**
```python
try:
    response = openai_client.chat.completions.create(...)
    return {'success': True, 'result': response.choices[0].message.content}
except openai.AuthenticationError:
    return {'success': False, 'error': 'API key validation failed', 
            'suggestion': 'Check your OpenAI API key configuration'}
except openai.RateLimitError:
    return {'success': False, 'error': 'Rate limit exceeded', 
            'suggestion': 'Please wait and try again'}
except Exception as e:
    return {'success': False, 'error': f'Unexpected error: {str(e)}',
            'suggestion': 'Please try again or contact support'}
```

## Language-Specific Implementation Patterns

### Python Implementation

**Project Structure**
```
project/
├── src/package_name/
│   ├── __init__.py
│   ├── config.py
│   ├── client.py
│   └── utils.py
├── tests/
│   ├── test_config.py
│   ├── test_client.py
│   └── conftest.py
├── requirements.txt
├── pyproject.toml (optional)
└── README.md
```

**Code Quality Tools**
- Use type hints throughout (`typing` module)
- Format with `black` and `isort`
- Lint with `pylint` or `flake8`
- Type check with `mypy`
- Test with `pytest` and `pytest-cov`

**Error Handling Pattern**
```python
class ConfigurationError(Exception):
    """Raised when configuration is invalid."""
    pass

def load_config(path: str) -> Dict[str, Any]:
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise ConfigurationError(f"Config file not found: {path}")
    except json.JSONDecodeError as e:
        raise ConfigurationError(f"Invalid JSON in config: {e}")
```

### JavaScript/Node.js Implementation

**Project Structure**
```
project/
├── src/
│   ├── config.js
│   ├── client.js
│   └── utils.js
├── tests/
│   ├── config.test.js
│   └── client.test.js
├── package.json
├── tsconfig.json (if using TypeScript)
└── README.md
```

**Code Quality Tools**
- Use TypeScript for type safety
- Format with Prettier
- Lint with ESLint
- Test with Jest or Mocha
- Use npm scripts for automation

**Error Handling Pattern**
```javascript
class ConfigurationError extends Error {
  constructor(message) {
    super(message);
    this.name = 'ConfigurationError';
  }
}

async function loadConfig(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    return JSON.parse(data);
  } catch (error) {
    if (error.code === 'ENOENT') {
      throw new ConfigurationError(`Config file not found: ${path}`);
    }
    if (error instanceof SyntaxError) {
      throw new ConfigurationError(`Invalid JSON in config: ${error.message}`);
    }
    throw error;
  }
}
```

### Go Implementation

**Project Structure**
```
project/
├── cmd/app/
│   └── main.go
├── internal/
│   ├── config/
│   ├── client/
│   └── utils/
├── pkg/
├── go.mod
├── go.sum
└── README.md
```

**Code Quality Tools**
- Format with `gofmt`
- Lint with `golint` and `go vet`
- Test with built-in testing package
- Use `go mod` for dependencies

**Error Handling Pattern**
```go
type ConfigError struct {
    Msg string
}

func (e *ConfigError) Error() string {
    return e.Msg
}

func LoadConfig(path string) (*Config, error) {
    data, err := ioutil.ReadFile(path)
    if err != nil {
        return nil, &ConfigError{Msg: fmt.Sprintf("Config file not found: %s", path)}
    }
    
    var config Config
    if err := json.Unmarshal(data, &config); err != nil {
        return nil, &ConfigError{Msg: fmt.Sprintf("Invalid JSON in config: %v", err)}
    }
    
    return &config, nil
}
```

## Documentation Standards

### 1. README Requirements

**Essential Sections**
- Project overview and purpose
- Quick start instructions
- Prerequisites and dependencies
- Configuration steps
- Usage examples
- Troubleshooting guide

**Writing Guidelines**
- Write for your least technical user
- Include actual command examples
- Show expected outputs
- Provide links to additional resources
- Keep instructions up to date

### 2. Code Documentation

**Function Documentation**
- Purpose and behavior
- Parameter descriptions with types
- Return value descriptions
- Exception/error conditions
- Usage examples for complex functions

**Class Documentation**
- Purpose and responsibilities
- Key attributes and their meanings
- Important methods and their usage
- Thread safety considerations
- Lifecycle management

### 3. API Documentation

**For External APIs**
- Authentication requirements
- Request/response formats
- Error codes and meanings
- Rate limiting information
- Example requests and responses

**For Internal APIs**
- Interface contracts
- Expected behaviors
- Error conditions
- Performance characteristics
- Versioning strategy

## Deployment and Operations

### 1. Configuration Management

**Environment-Specific Settings**
- Development, staging, production configurations
- Secret management strategy
- Configuration validation
- Environment variable documentation
- Default value strategy

**Deployment Artifacts**
- Dependency management files
- Configuration templates
- Setup scripts
- Health check endpoints
- Monitoring configurations

### 2. Monitoring and Logging

**Application Metrics**
- Performance metrics (response times, throughput)
- Error rates and types
- Resource utilization
- Business metrics
- Health check status

**Logging Strategy**
- Structured logging format
- Appropriate log levels
- Sensitive data handling
- Log rotation and retention
- Correlation identifiers

## Continuous Improvement

### 1. Specification Evolution

**Regular Review Process**
- Collect feedback from implementers
- Update based on real-world usage
- Clarify ambiguous requirements
- Add missing edge cases
- Improve examples and explanations

**Version Management**
- Track specification changes
- Maintain backward compatibility
- Document breaking changes
- Provide migration guides
- Archive obsolete versions

### 2. Implementation Feedback

**Common Issues Tracking**
- Frequently misunderstood requirements
- Implementation challenges
- Performance bottlenecks
- Security concerns
- Usability problems

**Best Practice Updates**
- Learn from implementation experiences
- Update guidelines based on new tools
- Incorporate community feedback
- Add new language support
- Improve development processes

## Environment Management and CUDA Considerations

### 1. Multi-Package Manager Support

**Document All Installation Paths**
```bash
# Pip installation
pip install torch torchvision

# Conda installation  
conda install pytorch torchvision pytorch-cuda=12.4 -c pytorch -c nvidia

# Mamba installation (preferred)
mamba install pytorch torchvision pytorch-cuda=12.4 -c pytorch -c nvidia
```

**Package Manager Preferences**
- **mamba > conda > pip** for complex dependencies
- Document why each manager might be needed
- Include version requirements and build strings
- Provide troubleshooting for conflicts

### 2. CUDA and GPU Environment Setup

**CUDA Detection and Verification**
```python
import torch

def check_cuda_environment():
    """Verify CUDA setup and provide diagnostic information."""
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"GPU device: {torch.cuda.get_device_name(0)}")
        print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    else:
        print("CUDA not available - running on CPU")
```

**Build String Verification**
```bash
# Check PyTorch build string - should contain "cuda" not "cpu"
python -c "import torch; print(torch.__version__)"
# Good: 2.1.0+cu121
# Bad:  2.1.0+cpu

# For conda/mamba users, check actual package info
conda list pytorch
# Look for build string containing "cuda"
```

**Common CUDA Issues and Solutions**
- **CPU-only PyTorch**: Reinstall with conda/mamba using cuda channel
- **CUDA version mismatch**: Use pytorch-cuda package for version specification
- **Driver incompatibility**: Update NVIDIA drivers or use compatible CUDA version
- **Memory errors**: Implement GPU memory monitoring and cleanup

### 3. Environment Verification Scripts

**Comprehensive Environment Check**
```python
def verify_environment():
    """Complete environment verification with actionable output."""
    issues = []
    
    # Check Python version
    if sys.version_info < (3, 8):
        issues.append("Python 3.8+ required")
    
    # Check CUDA setup
    if not torch.cuda.is_available():
        issues.append("CUDA not available - check PyTorch installation")
    
    # Check API keys
    if not os.path.exists('config/config.json'):
        issues.append("config/config.json not found - copy from template")
    
    # Report results
    if issues:
        print("❌ Environment Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nSee README.md for setup instructions")
    else:
        print("✅ Environment verification passed")
```

**Diagnostic Commands for Documentation**
```bash
# Include these in README.md for troubleshooting
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"
nvidia-smi  # For NVIDIA GPU users
```

### 4. Cross-Platform Considerations

**Path Handling**
```python
from pathlib import Path

# Use pathlib for cross-platform path handling
config_path = Path("config") / "config.json"
```

**Terminal Command Documentation**
- Use absolute paths in examples to avoid confusion
- Provide both Windows and Unix command examples where different
- Test instructions on multiple platforms
- Document platform-specific gotchas

This document should be updated regularly based on experience implementing specifications across different projects and technology stacks. 