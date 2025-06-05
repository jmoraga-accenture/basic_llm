# AI Testing Web Application - v2

A Flask web application for testing OpenAI models and neural network capabilities. This application provides a browser-based interface for running AI tests without requiring command-line interaction.

## Features

- **OpenAI Model Testing**: Test GPT-4o and GPT-4o Mini models with custom prompts
- **Neural Network Testing**: 4-layer Inception-based CNN architecture testing
- **GPU/CPU Detection**: Automatic hardware detection and performance monitoring
- **Real-time Results**: Live feedback and detailed test results
- **Responsive Design**: Clean, modern web interface

## Quick Start

### Prerequisites

- Python 3.8 or higher
- PyTorch compatible system (CPU or CUDA GPU)
- OpenAI API key

### Installation

1. **Clone and navigate to the v2 directory**:
   ```bash
   cd v2/
   ```

2. **Install dependencies**:
   
   **For CUDA GPU support - PIP Method** (recommended for CUDA 12.8):
   ```bash
   # For CUDA 12.8 (latest)
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
   pip install flask openai numpy
   ```
   
   **For CUDA GPU support - CONDA/MAMBA Method**:
   ```bash
   # Check your CUDA version first
   nvidia-smi  # Look for "CUDA Version" in output
   
   # Check available PyTorch CUDA versions
   conda search pytorch-cuda -c pytorch
   
   # Install PyTorch with CUDA support (adjust version as needed)
   # For CUDA 12.4-12.8 systems:
   conda install pytorch torchvision pytorch-cuda=12.4 -c pytorch -c nvidia
   
   # For CUDA 12.1 systems:
   conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia
   
   # Install other dependencies
   conda install flask openai numpy
   ```
   
   **⚠️ CRITICAL: Verify you got CUDA-enabled PyTorch:**
   ```bash
   # Check the build string - it should contain "cuda", not "cpu"
   conda list pytorch
   # Good: pytorch 2.5.1 py3.11_cuda12.4_cudnn9.1.0_0 pytorch
   # Bad:  pytorch 2.7.0 cpu_mkl_py311_he84fd7d_100 conda-forge
   
   # If you got CPU version, remove and reinstall:
   conda remove pytorch torchvision --yes
   conda install pytorch torchvision pytorch-cuda=12.4 -c pytorch -c nvidia
   ```
   
   **For CPU-only**:
   ```bash
   # PIP
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
   pip install flask openai numpy
   
   # CONDA
   conda install pytorch torchvision cpuonly -c pytorch
   conda install flask openai numpy
   ```

3. **Configure API key**:
   ```bash
   # Copy the template configuration file
   cp config/config.json.template config/config.json
   
   # Edit config/config.json and add your OpenAI API key
   # Replace "your-openai-api-key-here" with your actual API key
   ```

4. **Start the application**:
   ```bash
   python app.py
   ```

5. **Open your browser**:
   Navigate to `http://localhost:5000`

## Configuration

### API Key Setup

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Copy `config/config.json.template` to `config/config.json`
3. Replace `"your-openai-api-key-here"` with your actual API key:

```json
{
    "openai": {
        "api_key": "sk-your-actual-api-key-here"
    }
}
```

### GPU Setup and Verification

The application automatically detects CUDA-compatible GPUs. For optimal neural network testing:

**Check Your CUDA Version:**
```bash
nvidia-smi  # Look for "CUDA Version" in the output
```

**Verify PyTorch CUDA Installation:**
```bash
python -c "import torch; print(f'CUDA Available: {torch.cuda.is_available()}'); print(f'CUDA Version: {torch.version.cuda}'); print(f'Device Count: {torch.cuda.device_count()}')"
```

**Expected Output with GPU:**
```
CUDA Available: True
CUDA Version: 12.8
Device Count: 1
```

**If CUDA shows as unavailable:**
1. Verify your NVIDIA drivers are installed: `nvidia-smi`
2. Reinstall PyTorch with correct CUDA version (see installation steps above)
3. Check that your GPU is CUDA-compatible

## Usage

### OpenAI Model Testing

1. Select your preferred model (GPT-4o or GPT-4o Mini)
2. Enter your query in the text area
3. Click "Test OpenAI API"
4. View results including:
   - Model response
   - Token usage statistics
   - Response time
   - Error handling (if any)

### Neural Network Testing

1. Click "Run Neural Network Test"
2. The application will:
   - Create a 4-layer Inception-based CNN
   - Test GPU/CPU compatibility
   - Perform a forward pass with synthetic data
   - Display architecture details and performance metrics

## Architecture Details

### Neural Network Specification

The test creates a 4-layer Inception-based CNN:

1. **Layer 1**: Conv2d (3→64 channels, 7x7 kernel) + MaxPool2d
2. **Layer 2**: Inception Block (64→128 channels)
3. **Layer 3**: Inception Block (128→256 channels)  
4. **Layer 4**: Adaptive pooling + Fully connected classifier

**Test Parameters**:
- Input: Batch of 4 RGB images (224×224)
- Output: 10-class classification scores
- Parameters: ~13M trainable parameters

### Web Framework

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **API**: RESTful endpoints for testing operations
- **Real-time**: Asynchronous JavaScript for live updates

## Project Structure

```
v2/
├── app.py                    # Main Flask application
├── config/
│   ├── config.json.template  # API key template
│   └── config.json          # Your API keys (gitignored)
├── templates/
│   └── index.html           # Main web interface
├── static/                  # Static assets (CSS/JS embedded in HTML)
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## API Endpoints

### POST /api/openai_test
Test OpenAI models with custom prompts.

**Request Body**:
```json
{
    "model": "gpt-4o",
    "query": "Your prompt here"
}
```

**Response**:
```json
{
    "success": true,
    "model": "gpt-4o",
    "response": "AI response text",
    "response_time": 2.345,
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 50,
        "total_tokens": 60
    }
}
```

### POST /api/neural_network_test
Test neural network creation and execution.

**Response**:
```json
{
    "success": true,
    "device_used": "CUDA",
    "processing_time": 1.234,
    "architecture": [...],
    "model_stats": {
        "total_parameters": "13,456,789",
        "model_size_mb": 51.2
    },
    "memory_usage": {
        "memory_used_gb": 2.3,
        "memory_total_gb": 8.0
    }
}
```

## Troubleshooting

### Common Issues

1. **Configuration file not found**:
   - Ensure `config/config.json` exists
   - Copy from `config/config.json.template`

2. **OpenAI API errors**:
   - Verify your API key is correct
   - Check your OpenAI account has credits
   - Ensure internet connectivity

3. **PyTorch/CUDA issues**:
   - **CUDA not detected**: Run `python -c "import torch; print(torch.cuda.is_available())"`
   - **Wrong PyTorch build**: Check build string with `conda list pytorch`
   - **CPU version installed**: Remove and reinstall with CUDA version
   - **GPU out of memory**: Neural network will automatically fall back to CPU
   - **No NVIDIA GPU**: Application works fine with CPU-only PyTorch
   
   **Quick CUDA fix - PIP users:**
   ```bash
   pip uninstall torch torchvision
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
   ```
   
   **Quick CUDA fix - CONDA/MAMBA users:**
   ```bash
   conda remove pytorch torchvision --yes
   conda install pytorch torchvision pytorch-cuda=12.4 -c pytorch -c nvidia
   ```
   
   **Debug PyTorch installation:**
   ```bash
   python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA Available: {torch.cuda.is_available()}'); print(f'CUDA Version: {torch.version.cuda}'); print(f'Device Name: {torch.cuda.get_device_name() if torch.cuda.is_available() else \"CPU\"}')"
   ```

4. **Port already in use**:
   - Change the port in `app.py`: `app.run(port=5001)`
   - Or kill the process using port 5000

### Logs and Debugging

- Check the terminal where you ran `python app.py` for error messages
- Browser developer console shows client-side errors
- Flask debug mode is enabled by default for detailed error pages

## Security Notes

- **API Keys**: Never commit `config/config.json` to version control
- **Local Use**: Application is designed for local development only
- **Production**: Additional security measures needed for production deployment

## License

Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

## Support

For issues related to:
- **OpenAI API**: Check [OpenAI Documentation](https://platform.openai.com/docs)
- **PyTorch**: Check [PyTorch Documentation](https://pytorch.org/docs/)
- **Flask**: Check [Flask Documentation](https://flask.palletsprojects.com/)

This application implements the specifications defined in `SPECIFICATIONS.md` and follows the development framework outlined in the project root. 
This application implements the specifications defined in `SPECIFICATIONS.md` and follows the development framework outlined in the project root. 