# DEFAULTS.md
# SpecFirst Development Defaults

This file provides concrete technical defaults prioritizing **Simplicity → Robustness → Standards**. LLMs have no architectural preferences, so these defaults guide technology choices based on project complexity and user experience levels.

## Decision Hierarchy

**Priority Order**: Simplicity → Robustness → Standards
1. **Simplicity**: Choose the minimal solution that meets requirements
2. **Robustness**: Scale up only when simplicity introduces reliability risks  
3. **Standards**: Apply industry standards only when robustness demands it

**User Experience Determines Complexity**:
- **Beginner projects**: Stick to simplicity defaults
- **Intermediate projects**: Add robustness when needed
- **Advanced projects**: Apply standards for enterprise requirements

## Technology Stack Defaults

### Web Application Stack (Simplicity → Robustness → Standards)

#### Frontend 
- **Simplicity**: Single HTML file with vanilla CSS/JavaScript
- **Robustness**: Add bundling (Vite) when file size/complexity grows
- **Standards**: React/TypeScript when team collaboration or complex state management needed

#### Backend
- **Simplicity**: Static hosting + serverless functions (Netlify/Vercel functions)
- **Robustness**: Flask/FastAPI when persistent state or complex logic required
- **Standards**: Django/Express with databases when multi-user enterprise features needed

#### Data Storage
- **Simplicity**: Browser localStorage, file download/upload for persistence
- **Robustness**: SQLite for structured data, file-based JSON for configuration
- **Standards**: PostgreSQL when concurrent access, transactions, or analytics required

#### API Design
- **Simplicity**: Direct function calls, form submissions, file operations
- **Robustness**: Simple REST endpoints (GET/POST only) with JSON
- **Standards**: Full RESTful API with proper HTTP methods, OpenAPI documentation

#### Authentication
- **Simplicity**: None (local-first applications)
- **Robustness**: Simple password protection, basic auth
- **Standards**: JWT tokens, OAuth2, proper session management

### Python Development (Simplicity → Robustness → Standards)

#### Environment Setup
- **Simplicity**: Python 3.9+ with pip, basic requirements.txt
- **Robustness**: Auto-detect mamba>conda>pip, virtual environments, hardware probing
- **Standards**: Reproducible conda environments, dependency locking, CI/CD integration

#### Code Quality
- **Simplicity**: Basic PEP 8, clear function names, simple docstrings
- **Robustness**: Type hints for public APIs, comprehensive error handling
- **Standards**: Full type coverage, Google-style docstrings, automated formatting

#### Testing
- **Simplicity**: Single test file, manual verification of primary use case
- **Robustness**: pytest with basic test coverage, automated CI
- **Standards**: Full test suite, coverage reporting, performance testing

### AI/ML Integration (Simplicity → Robustness → Standards)

#### Large Language Models (LLMs)
- **Simplicity**: OpenAI GPT-3.5-turbo with direct API calls, basic error handling
- **Robustness**: OpenAI GPT-4 with structured prompts, JSON validation, fallback to 3.5-turbo
- **Standards**: Multiple providers (OpenAI, Anthropic, local models), model selection, rate limiting

#### Traditional Machine Learning
- **Simplicity**: scikit-learn with basic models (LinearRegression, RandomForest, SVM)
- **Robustness**: scikit-learn pipelines, cross-validation, hyperparameter tuning
- **Standards**: MLflow for experiment tracking, model versioning, automated evaluation

#### Neural Networks / Deep Learning
- **Simplicity**: PyTorch with pretrained models (torchvision, transformers), minimal training
- **Robustness**: Custom PyTorch models, GPU acceleration, basic training loops
- **Standards**: PyTorch Lightning, distributed training, MLOps pipelines, model monitoring

#### AI Agents / Workflows
- **Simplicity**: Direct LLM calls with simple prompt chaining
- **Robustness**: LangChain for agent frameworks, memory, tool integration
- **Standards**: Multi-agent systems, planning algorithms, observability, human-in-the-loop

#### Computer Vision
- **Simplicity**: OpenCV for basic image processing, PIL for simple operations
- **Robustness**: torchvision pretrained models, custom CNN architectures
- **Standards**: Multi-modal models, real-time processing, edge deployment

#### Natural Language Processing
- **Simplicity**: Basic string processing, regex patterns, simple sentiment analysis
- **Robustness**: spaCy for NLP pipelines, sentence transformers for embeddings
- **Standards**: Custom transformer models, fine-tuning, domain-specific models

#### Data Processing for AI
- **Simplicity**: pandas for data manipulation, numpy for numerical operations
- **Robustness**: Efficient data pipelines, feature engineering, data validation
- **Standards**: Apache Spark, data versioning (DVC), automated feature stores

#### Model Deployment
- **Simplicity**: Local inference, simple Flask/FastAPI endpoints
- **Robustness**: Docker containers, basic monitoring, batch processing
- **Standards**: Kubernetes, model serving platforms (TorchServe), A/B testing

### AI/ML Code Examples

#### Simplicity: Basic ML with scikit-learn
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Load data
data = pd.read_csv('data.csv')
X = data.drop('target', axis=1)
y = data['target']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

#### Robustness: PyTorch with GPU support
```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

model = SimpleNet(784, 128, 10).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())
```

#### Standards: LangChain agent with tools
```python
from langchain.agents import create_openai_functions_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage

def calculator(expression: str) -> str:
    """Calculate mathematical expressions safely."""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Calculate mathematical expressions"
    )
]

llm = ChatOpenAI(model="gpt-4")
system_message = SystemMessage(content="You are a helpful assistant with access to tools.")

agent = create_openai_functions_agent(
    llm=llm,
    tools=tools,
    system_message=system_message
)
```

### AI/ML Environment Setup by Complexity

#### Simplicity: Basic pip installation
```bash
# Simple pip-based setup for personal projects
pip install numpy pandas scikit-learn openai

# For basic ML projects - CPU only
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

#### Robustness: Environment probing with mamba/conda
```bash
# Setup script that probes environment and installs accordingly
#!/bin/bash

# Check if mamba is available (preferred)
if command -v mamba &> /dev/null; then
    INSTALLER="mamba"
elif command -v conda &> /dev/null; then
    INSTALLER="conda"
else
    INSTALLER="pip"
    echo "Warning: Using pip. Consider installing mamba for better dependency resolution."
fi

# Probe for CUDA availability
if nvidia-smi &> /dev/null; then
    echo "CUDA detected, installing GPU-enabled packages"
    if [ "$INSTALLER" = "pip" ]; then
        pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
    else
        $INSTALLER install pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
    fi
else
    echo "No CUDA detected, installing CPU-only packages"
    if [ "$INSTALLER" = "pip" ]; then
        pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
    else
        $INSTALLER install pytorch torchvision cpuonly -c pytorch
    fi
fi

# Install other dependencies
$INSTALLER install numpy pandas scikit-learn
pip install openai langchain  # These are usually pip-only
```

#### Standards: Comprehensive environment management
```yaml
# environment.yml for reproducible conda/mamba environments
name: ai-project
channels:
  - pytorch
  - nvidia
  - conda-forge
dependencies:
  - python=3.9
  - numpy
  - pandas
  - scikit-learn
  - pytorch-cuda=11.8  # Will fallback to CPU if no CUDA
  - pytorch
  - torchvision
  - pytorch-lightning
  - transformers
  - pip
  - pip:
    - openai>=1.0.0
    - langchain>=0.1.0
    - mlflow>=2.8.0
    - wandb>=0.16.0

# Setup with: mamba env create -f environment.yml
```

### Environment Detection Patterns

#### Python Environment Probe Script
```python
# setup_check.py - Environment validation
import sys
import subprocess
import importlib.util

def check_package_manager():
    """Detect available package managers in priority order."""
    managers = [
        ('mamba', 'Fastest conda alternative'),
        ('conda', 'Standard conda'),
        ('pip', 'Python package installer')
    ]
    
    for manager, description in managers:
        if subprocess.run(['which', manager], capture_output=True).returncode == 0:
            print(f"✅ Found {manager}: {description}")
            return manager
    
    raise RuntimeError("No package manager found!")

def check_gpu_support():
    """Probe for GPU/CUDA availability."""
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ NVIDIA GPU detected")
            return True
    except FileNotFoundError:
        pass
    
    print("ℹ️  No GPU detected, using CPU-only packages")
    return False

def install_pytorch(manager, has_gpu):
    """Install PyTorch with appropriate backend."""
    if manager == 'pip':
        if has_gpu:
            cmd = ['pip', 'install', 'torch', 'torchvision', '--index-url', 'https://download.pytorch.org/whl/cu118']
        else:
            cmd = ['pip', 'install', 'torch', 'torchvision', '--index-url', 'https://download.pytorch.org/whl/cpu']
    else:
        if has_gpu:
            cmd = [manager, 'install', 'pytorch', 'torchvision', 'pytorch-cuda=11.8', '-c', 'pytorch', '-c', 'nvidia']
        else:
            cmd = [manager, 'install', 'pytorch', 'torchvision', 'cpuonly', '-c', 'pytorch']
    
    print(f"Installing PyTorch: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    manager = check_package_manager()
    has_gpu = check_gpu_support()
    install_pytorch(manager, has_gpu)
    print("✅ Environment setup complete!")
```

### GPU/CUDA Considerations (AI/ML Projects)

#### Simplicity: CPU-only development
```python
# Use CPU for prototyping and small datasets
device = 'cpu'
model = model.to(device)

# For PyTorch, install CPU version:
# pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

#### Robustness: GPU acceleration when available
```python
# Auto-detect GPU availability
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name()}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

model = model.to(device)
```

#### Standards: Multi-GPU and optimization
```python
# Multi-GPU training with PyTorch Lightning
import pytorch_lightning as pl

class LitModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = YourModel()
    
    def training_step(self, batch, batch_idx):
        # Training logic
        pass

# Train on multiple GPUs
trainer = pl.Trainer(
    accelerator='gpu',
    devices=-1,  # Use all available GPUs
    strategy='ddp'  # Distributed Data Parallel
)
```

### Environment Setup for AI/ML

#### CUDA Installation Verification
```bash
# Check CUDA availability
nvidia-smi

# Verify PyTorch CUDA support
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"
python -c "import torch; print(f'Version: {torch.version.cuda}')"
```

#### Package Manager Selection Strategy
```python
# Automatic package manager detection and setup
def setup_ai_environment():
    """Setup AI/ML environment following mamba > conda > pip priority."""
    
    # 1. Detect available package managers
    package_managers = []
    for manager in ['mamba', 'conda', 'pip']:
        if shutil.which(manager):
            package_managers.append(manager)
    
    if not package_managers:
        raise RuntimeError("No package managers found!")
    
    primary_manager = package_managers[0]  # Highest priority available
    print(f"Using {primary_manager} for package management")
    
    # 2. Probe hardware capabilities
    has_cuda = check_cuda_availability()
    
    # 3. Install packages based on capabilities and manager
    if primary_manager in ['mamba', 'conda']:
        install_with_conda_family(primary_manager, has_cuda)
    else:
        install_with_pip(has_cuda)

def install_with_conda_family(manager, has_cuda):
    """Install using mamba/conda with proper channel priorities."""
    base_cmd = [manager, 'install', '-c', 'pytorch', '-c', 'nvidia', '-c', 'conda-forge']
    
    if has_cuda:
        packages = ['pytorch', 'torchvision', 'pytorch-cuda=11.8']
    else:
        packages = ['pytorch', 'torchvision', 'cpuonly']
    
    subprocess.run(base_cmd + packages, check=True)
    
    # Install pip-only packages
    pip_packages = ['openai>=1.0.0', 'langchain>=0.1.0']
    subprocess.run(['pip', 'install'] + pip_packages, check=True)
```

## Project Structure (Simplicity → Robustness → Standards)

### Simplicity Structure (Single-file applications)
```
project_root/
├── index.html              # Complete application in one file
├── README.md              # Setup and usage guide
└── SPECIFICATIONS.md      # Project specification
```

### Robustness Structure (Separated concerns)
```
project_root/
├── SPECIFICATIONS.md       # Project specification  
├── README.md              # Setup and usage guide
├── .gitignore             # Basic exclusions
├── index.html             # Main HTML file
├── style.css              # Styles
├── script.js              # JavaScript logic
├── app.py                 # Backend (if needed)
├── requirements.txt       # Dependencies
└── test.py               # Basic functionality test
```

### Standards Structure (Full development framework)
```
project_root/
├── .cursorrules           # Development framework
├── SPECIFICATIONS.md      # Complete project specification
├── DEFAULTS.md           # Technical defaults  
├── README.md             # Comprehensive guide
├── .gitignore            # Security exclusions
├── requirements.txt      # Dependencies
├── config/
│   ├── config.json.template # Configuration template
│   └── .env.example     # Environment variables
├── src/
│   ├── __init__.py
│   ├── app.py           # Main application
│   ├── api/             # API endpoints
│   ├── services/        # Business logic
│   └── utils/           # Utilities
├── static/              # Static assets
├── templates/           # HTML templates
├── tests/
│   ├── test_primary_case.py # Main test
│   └── conftest.py      # Test configuration
└── docs/                # Documentation
```

## Configuration (Simplicity → Robustness → Standards)

### Security Approach
- **Simplicity**: Hardcoded API keys for personal projects (with clear warnings)
- **Robustness**: Environment variables, basic input validation
- **Standards**: Comprehensive credential management, input sanitization, audit logging

### Configuration Storage
- **Simplicity**: Direct variables in code with comments for required changes
- **Robustness**: config.json files with templates, environment variable fallbacks
- **Standards**: Multiple environment support, secure secret management, validation

### Configuration Examples

#### Simplicity Example
```javascript
// In HTML <script> tag
const OPENAI_API_KEY = 'sk-your-key-here'; // ⚠️ Change this before deploying!
const API_BASE = 'https://api.openai.com/v1';
```

#### Robustness Example (Environment-aware setup)
```python
# setup.py - Probes environment and configures accordingly
import os
import subprocess
import shutil

def detect_environment():
    """Detect available tools and hardware capabilities."""
    config = {
        'package_manager': None,
        'has_cuda': False,
        'python_version': None
    }
    
    # Detect package manager (priority: mamba > conda > pip)
    for manager in ['mamba', 'conda', 'pip']:
        if shutil.which(manager):
            config['package_manager'] = manager
            break
    
    # Probe for CUDA
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True)
        config['has_cuda'] = result.returncode == 0
    except FileNotFoundError:
        config['has_cuda'] = False
    
    return config

# config.py - Load configuration with environment detection
def load_config():
    env_config = detect_environment()
    
    return {
        'openai_api_key': os.getenv('OPENAI_API_KEY', 'sk-required-change-me'),
        'debug': os.getenv('DEBUG', 'False').lower() == 'true',
        'host': os.getenv('HOST', '127.0.0.1'),
        'port': int(os.getenv('PORT', 5000)),
        'device': 'cuda' if env_config['has_cuda'] else 'cpu',
        'package_manager': env_config['package_manager']
    }
```

#### Standards Example
```python
# config/config.py
import os
from typing import Dict, Any

def load_config() -> Dict[str, Any]:
    """Load configuration with validation and secure defaults."""
    config = {
        'openai_api_key': os.getenv('OPENAI_API_KEY'),
        'database_url': os.getenv('DATABASE_URL', 'postgresql://localhost/appdb'),
        'debug': os.getenv('DEBUG', 'False').lower() == 'true',
        'host': os.getenv('HOST', '127.0.0.1'),
        'port': int(os.getenv('PORT', 5000)),
        'secret_key': os.getenv('SECRET_KEY', 'dev-only-change-in-production')
    }
    
    # Validate required keys
    if not config['openai_api_key']:
        raise ValueError("OPENAI_API_KEY environment variable required")
    
    return config
```

## API Design (Simplicity → Robustness → Standards)

### Simplicity: No API (Direct operations)
```javascript
// Direct file operations, no server needed
function saveSpecification(text) {
    localStorage.setItem('specification', text);
}

function analyzeText(text) {
    // Simple client-side patterns
    const ambiguities = text.match(/maybe|might|should|probably/gi);
    return { score: ambiguities ? ambiguities.length : 0 };
}
```

### Robustness: Minimal API
```python
# app.py - Simple Flask endpoints
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json['text']
    result = analyze_with_openai(text)
    return {'success': True, 'data': result}
```

### Standards: Full RESTful API
```python
# Comprehensive API with proper structure
@app.route('/api/sessions', methods=['GET', 'POST'])
@app.route('/api/sessions/<id>', methods=['GET', 'PUT', 'DELETE'])
def sessions(id=None):
    # Full CRUD operations with validation, error handling
    pass

# Response format:
{
  "success": true,
  "data": { ... },
  "message": "Operation completed",
  "timestamp": "2025-01-XX...",
      "request_id": "uuid-here"
  }
  ```

## Universal Implementation Principles

### Copyright Headers
Ask user for their name, email, and current date to create:
```python
# Copyright (c) [YEAR], [NAME] ([EMAIL])
```

### Error Handling Philosophy
- **Simplicity**: Basic try/catch with console.log or print statements
- **Robustness**: User-friendly messages, graceful degradation
- **Standards**: Comprehensive error types, logging, monitoring

### Documentation Requirements
- **Simplicity**: README with "how to run" instructions
- **Robustness**: Setup guide, troubleshooting section, examples
- **Standards**: Complete API docs, architecture diagrams, contribution guidelines

### Testing Strategy
- **Simplicity**: Manual testing of primary use case
- **Robustness**: Automated test for main workflow, basic edge cases
- **Standards**: Comprehensive test suite, CI/CD, performance testing

## When to Escalate Complexity

### Move from Simplicity → Robustness when:
- Multiple users will use the application
- Data persistence beyond browser session needed
- Error recovery becomes important
- Performance becomes a concern

### Move from Robustness → Standards when:
- Team collaboration required
- Production deployment with SLA requirements
- Security/compliance requirements
- Integration with enterprise systems

## Quick Decision Matrix

| Project Scope | Frontend | Backend | Data | AI/ML | Package Mgmt | Testing |
|--------------|----------|---------|------|-------|--------------|---------|
| **Personal Tool** | Single HTML | None/Serverless | localStorage | pip: sklearn/openai | pip | Manual |
| **Small Team** | HTML + CSS/JS | Flask/FastAPI | SQLite/JSON | mamba>conda: PyTorch+LangChain | mamba>conda>pip | Basic automated |
| **Production App** | React/TypeScript | Full framework | PostgreSQL | conda envs: Lightning+MLOps | mamba with env.yml | Comprehensive |
| **Research/Experiment** | Jupyter Notebook | Local scripts | CSV/Pickle | mamba: Full ML stack | mamba+CUDA probing | Experimental validation |
| **AI Product** | React/Streamlit | FastAPI/Flask | Vector DB + SQL | conda: LLMs+Custom models | mamba with CI/CD | Model evaluation |

## .gitignore by Complexity Level

### Simplicity
```
# Nothing to ignore for single-file HTML projects
```

### Robustness  
```
*.pyc
__pycache__/
.env
config.json
```

### Standards
```
# Credentials and Config
config/config.json
.env
*.key
*.pem

# Dependencies  
node_modules/
__pycache__/
*.pyc
.pytest_cache/

# Conda/Mamba environments
.conda/
envs/
*.tar.bz2

# IDE and OS
.vscode/settings.json
.DS_Store
Thumbs.db

# Build and Deploy
dist/
build/
*.log

# ML/AI specific
*.ckpt
*.pth
wandb/
mlruns/
```

## Package Management Consistency Rules

### Always Follow Priority: mamba > conda > pip
1. **Simplicity projects**: Use pip only when it's truly a single-file project
2. **Robustness projects**: Auto-detect and use highest available manager
3. **Standards projects**: Use mamba/conda with environment.yml for reproducibility

### Environment Probing Pattern
```python
# Consistent detection pattern for all robustness+ projects
def get_package_manager():
    for manager in ['mamba', 'conda', 'pip']:
        if shutil.which(manager):
            return manager
    raise RuntimeError("No package manager available")

def get_pytorch_install_cmd(manager, has_cuda):
    if manager == 'pip':
        index = '--index-url https://download.pytorch.org/whl/cu118' if has_cuda else '--index-url https://download.pytorch.org/whl/cpu'
        return ['pip', 'install', 'torch', 'torchvision', index]
    else:
        packages = ['pytorch', 'torchvision']
        if has_cuda:
            packages.append('pytorch-cuda=11.8')
            channels = ['-c', 'pytorch', '-c', 'nvidia']
        else:
            packages.append('cpuonly')
            channels = ['-c', 'pytorch']
        return [manager, 'install'] + packages + channels
```

---

**Usage**: Start with Simplicity defaults. Only add complexity when requirements clearly demand it. For AI/ML projects, prefer mamba>conda>pip and always probe for CUDA before package installation. LLMs should follow this hierarchy unless the user explicitly requests a different approach. 