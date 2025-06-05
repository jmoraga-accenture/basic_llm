# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Project Specifications

This document describes the requirements and behavior for a Basic OpenAI API Client with GPU Testing capabilities. These specifications are language-agnostic and can be implemented in any programming language.

## Project Overview

Create a modular system that provides two main capabilities:
1. **OpenAI API Client**: A clean interface for interacting with OpenAI's services
2. **GPU Testing Framework**: Tools for testing and monitoring GPU/compute capabilities

The system should be secure, well-documented, and follow best practices for the chosen implementation language.

## Core Requirements

### 1. Configuration Management

**Purpose**: Securely manage API keys and system settings

**Requirements**:
- Load configuration from a structured file (JSON, YAML, or similar)
- Support environment variable overrides for sensitive data
- Validate configuration before use
- Provide meaningful error messages for missing or invalid settings
- Never expose sensitive data in logs or error messages

**Configuration Structure**:
- OpenAI API key (required)
- Model selection (default: gpt-4o)
- Temperature setting (default: 0.7)
- Maximum tokens (default: 1000)

**Behavior**:
- If API key is missing, provide clear instructions to user
- Allow configuration file to be a template that users copy and customize
- Support both file-based and environment-based configuration

### 2. OpenAI API Client

**Purpose**: Provide a clean interface for OpenAI API interactions

**Requirements**:
- Send chat completion requests to OpenAI
- Handle API errors gracefully
- Return structured responses with success/failure status
- Support configurable parameters (model, temperature, max tokens)
- Include usage statistics when available
- Implement connection testing functionality

**Expected Behavior**:
- When API call succeeds: return response text, usage info, and model used
- When API call fails: return error type and user-friendly error message
- Connection test should verify API connectivity with minimal resource usage
- All network operations should have reasonable timeouts
- Should handle rate limiting and common API errors

### 3. GPU Detection and Monitoring

**Purpose**: Detect and report on available compute resources

**Requirements**:
- Detect if GPU acceleration is available
- Report GPU specifications and capabilities
- Monitor GPU memory usage
- Provide system information relevant to compute tasks
- Work correctly whether GPU is available or not

**Information to Gather**:
- GPU availability (yes/no)
- GPU model names and compute capabilities
- Total, free, and used GPU memory
- Number of available GPUs
- System platform and runtime information
- Acceleration framework version (CUDA, OpenCL, etc.)

**Behavior**:
- Gracefully handle systems without GPU support
- Provide formatted output suitable for human reading
- Return structured data suitable for programmatic use
- Include memory information in human-readable units (GB, not bytes)

### 4. Neural Network Testing

**Purpose**: Verify compute capabilities with a simple neural network

**Requirements**:
- Implement a simple feedforward neural network
- Support both CPU and GPU execution
- Measure inference performance
- Demonstrate tensor operations
- Provide model architecture information

**Model Specifications**:
- Input layer: 784 features (representing flattened 28x28 images)
- Hidden layers: Two layers with 128 neurons each
- Output layer: 10 neurons (for classification tasks)
- Activation: ReLU between layers, no activation on output
- Should automatically use best available compute device

**Testing Requirements**:
- Generate synthetic test data
- Measure inference time
- Report throughput (samples per second)
- Verify model runs on available hardware
- Display model architecture and parameter count

### 5. Performance Testing

**Purpose**: Benchmark compute performance

**Requirements**:
- Test basic tensor operations (matrix multiplication)
- Measure GPU vs CPU performance differences
- Test model inference speed
- Report timing results with appropriate precision
- Warm up hardware before meaningful measurements

**Metrics to Report**:
- Matrix multiplication time for large matrices
- Model inference time
- Throughput measurements
- Memory usage during operations
- Device utilization

## System Architecture

### Component Organization

**Configuration Layer**:
- Handles all settings and credentials
- Validates input parameters
- Manages environment integration

**API Client Layer**:
- Abstracts OpenAI API interactions
- Handles authentication and requests
- Manages errors and retries

**Compute Layer**:
- Manages GPU/CPU detection
- Handles device selection and management
- Provides hardware monitoring

**Testing Layer**:
- Implements neural network models
- Conducts performance benchmarks
- Reports results and metrics

### Data Flow

1. **Startup**: Load and validate configuration
2. **API Testing**: Test OpenAI connectivity and basic functionality
3. **Hardware Detection**: Scan for available compute resources
4. **Performance Testing**: Run benchmarks on detected hardware
5. **Reporting**: Display results in human-readable format

## User Experience Requirements

### Command Line Interface

**Primary Test Script** (equivalent to test_gpu.py):
- Display system information and GPU capabilities
- Test basic tensor operations with timing
- Create and test neural network model
- Show model architecture and performance metrics
- Provide clear success/failure indicators

**API Test Script** (equivalent to main.py):
- Verify configuration is properly loaded
- Test OpenAI API connectivity
- Send sample query and display response
- Show usage statistics
- Provide helpful error messages for common issues

### Output Format

**GPU Information Display**:
```
GPU Information:
============================================================
CUDA Available: Yes/No
CUDA Version: X.X
Number of GPUs: N

GPU 0: [GPU Name]
  Memory Total: X.X GB
  Memory Free: X.X GB
  Memory Used: X.X GB
  Compute Capability: X.X

System Information:
  Platform: [Platform Info]
  Runtime Version: [Version]
```

**Performance Results**:
```
Testing GPU Functionality
==================================================
Matrix multiplication (1000x1000): 0.0123 seconds
Using device: [CPU/GPU]

Testing Model
==================================================
Model Architecture:
--------------------------------------------------
Layer 1: Linear (784 -> 128) + ReLU
Layer 2: Linear (128 -> 128) + ReLU  
Layer 3: Linear (128 -> 10)
--------------------------------------------------
Total Parameters: 123,456
Model Size: 0.47 MB

Inference Results:
Input shape: (64, 784)
Output shape: (64, 10)
Inference time: 0.0045 seconds
Samples per second: 14,222.2
```

## Security Requirements

### Credential Management
- Never hardcode API keys in source code
- Support secure environment variable loading
- Exclude configuration files from version control
- Provide secure configuration templates

### Error Handling
- Never expose sensitive information in error messages
- Provide helpful guidance without revealing system internals
- Log errors appropriately without exposing credentials
- Handle network timeouts and failures gracefully

## Testing Requirements

### Unit Testing
- Test each component independently
- Mock external dependencies (APIs, hardware)
- Verify error handling paths
- Test configuration validation

### Integration Testing
- Test component interactions
- Verify end-to-end workflows
- Test with and without GPU hardware
- Validate API integration

### Test Coverage
- All public interfaces should be tested
- Error conditions should be tested
- Performance characteristics should be verified
- Different hardware configurations should be tested

## Documentation Requirements

### User Documentation
- Quick start guide with setup instructions
- Configuration examples and templates
- Troubleshooting guide for common issues
- Requirements and dependencies

### Developer Documentation
- Architecture overview
- Component interfaces
- Extension points for new features
- Coding standards and practices

## Installation and Setup

### Environment Requirements
- Support for virtual/isolated environments
- Dependency management system
- Development tool integration
- Cross-platform compatibility

### Dependencies
- Machine learning/tensor computation framework
- HTTP client library for API requests
- JSON/YAML parsing capability
- Testing framework
- Documentation tools

### Setup Process
1. Create isolated environment
2. Install dependencies
3. Copy and customize configuration template
4. Run initial tests to verify setup
5. Provide feedback on successful installation

## Performance Criteria

### Acceptable Performance
- API responses within 30 seconds
- GPU detection completes within 5 seconds
- Model inference completes within 1 second for test data
- Memory usage remains reasonable for target system

### Error Recovery
- Graceful degradation when GPU unavailable
- Fallback to CPU when GPU operations fail
- Clear error messages for configuration issues
- Automatic retry for transient network errors

This specification defines the behavior and requirements without prescribing implementation details, allowing flexibility in language choice and technical approach. 