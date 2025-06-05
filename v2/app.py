# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""AI Testing Web Application - v2

A Flask web application for testing OpenAI models and neural network capabilities.
Implements specifications from SPECIFICATIONS.md.
"""

import json
import time
import traceback
from pathlib import Path
from typing import Dict, Any, Tuple

import torch
import torch.nn as nn
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configuration
CONFIG_PATH = Path("config/config.json")
CONFIG_TEMPLATE_PATH = Path("config/config.json.template")


class InceptionBlock(nn.Module):
    """Basic Inception-like block for demonstration."""
    
    def __init__(self, in_channels: int, out_channels: int) -> None:
        super(InceptionBlock, self).__init__()
        
        # 1x1 conv branch
        self.branch1x1 = nn.Conv2d(in_channels, out_channels // 4, kernel_size=1)
        
        # 3x3 conv branch
        self.branch3x3_1 = nn.Conv2d(in_channels, out_channels // 4, kernel_size=1)
        self.branch3x3_2 = nn.Conv2d(out_channels // 4, out_channels // 4, kernel_size=3, padding=1)
        
        # 5x5 conv branch (using two 3x3)
        self.branch5x5_1 = nn.Conv2d(in_channels, out_channels // 4, kernel_size=1)
        self.branch5x5_2 = nn.Conv2d(out_channels // 4, out_channels // 4, kernel_size=3, padding=1)
        
        # Max pool branch
        self.branch_pool = nn.Conv2d(in_channels, out_channels // 4, kernel_size=1)
        self.max_pool = nn.MaxPool2d(kernel_size=3, stride=1, padding=1)
        
        self.relu = nn.ReLU(inplace=True)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 1x1 branch
        branch1x1 = self.relu(self.branch1x1(x))
        
        # 3x3 branch
        branch3x3 = self.relu(self.branch3x3_1(x))
        branch3x3 = self.relu(self.branch3x3_2(branch3x3))
        
        # 5x5 branch
        branch5x5 = self.relu(self.branch5x5_1(x))
        branch5x5 = self.relu(self.branch5x5_2(branch5x5))
        
        # Pool branch
        branch_pool = self.max_pool(x)
        branch_pool = self.relu(self.branch_pool(branch_pool))
        
        # Concatenate all branches
        outputs = [branch1x1, branch3x3, branch5x5, branch_pool]
        return torch.cat(outputs, 1)


class DemoInceptionCNN(nn.Module):
    """4-layer CNN with Inception-based architecture for demonstration."""
    
    def __init__(self, num_classes: int = 10) -> None:
        super(DemoInceptionCNN, self).__init__()
        
        # Layer 1: Initial convolution
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3)
        self.pool1 = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        
        # Layer 2: Inception block 1
        self.inception1 = InceptionBlock(64, 128)
        
        # Layer 3: Inception block 2
        self.inception2 = InceptionBlock(128, 256)
        
        # Layer 4: Final classification layers
        self.adaptive_pool = nn.AdaptiveAvgPool2d((7, 7))
        self.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(256 * 7 * 7, 1024),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(1024, num_classes)
        )
        
        self.relu = nn.ReLU(inplace=True)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Layer 1
        x = self.relu(self.conv1(x))
        x = self.pool1(x)
        
        # Layer 2
        x = self.inception1(x)
        
        # Layer 3
        x = self.inception2(x)
        
        # Layer 4
        x = self.adaptive_pool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        
        return x


def load_config() -> Dict[str, Any]:
    """Load configuration from config file."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_PATH}. "
            f"Please copy {CONFIG_TEMPLATE_PATH} to {CONFIG_PATH} and add your API key."
        )
    
    try:
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file: {e}")


def get_gpu_info() -> Dict[str, Any]:
    """Get GPU information and availability."""
    gpu_info = {
        "cuda_available": torch.cuda.is_available(),
        "device_count": 0,
        "current_device": "CPU",
        "memory_total": 0,
        "memory_free": 0,
        "memory_used": 0,
        "device_name": "CPU"
    }
    
    if torch.cuda.is_available():
        gpu_info.update({
            "device_count": torch.cuda.device_count(),
            "current_device": f"GPU ({torch.cuda.get_device_name()})",
            "device_name": torch.cuda.get_device_name(),
        })
        
        # Get memory info
        memory_info = torch.cuda.mem_get_info()
        gpu_info.update({
            "memory_free": memory_info[0],
            "memory_total": memory_info[1],
            "memory_used": memory_info[1] - memory_info[0]
        })
    
    return gpu_info


@app.route('/')
def index():
    """Render the main application page."""
    return render_template('index.html')


@app.route('/api/openai_test', methods=['POST'])
def openai_test():
    """Test OpenAI API with user query."""
    try:
        data = request.get_json()
        model = data.get('model', 'gpt-4o')
        query = data.get('query', '')
        
        if not query.strip():
            return jsonify({"success": False, "error": "Query cannot be empty"})
        
        # Load configuration
        config = load_config()
        api_key = config.get('openai', {}).get('api_key')
        
        if not api_key:
            return jsonify({
                "success": False, 
                "error": "OpenAI API key not found in configuration"
            })
        
        # Set up OpenAI client
        client = openai.OpenAI(api_key=api_key)
        
        # Record start time
        start_time = time.time()
        
        # Make API call
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": query}],
            max_tokens=1000,
            temperature=0.7
        )
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Extract response data
        result = {
            "success": True,
            "model": response.model,
            "query": query,
            "response": response.choices[0].message.content,
            "response_time": round(response_time, 3),
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        }
        
        return jsonify(result)
        
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return jsonify({
            "success": False,
            "error": str(e),
            "error_type": type(e).__name__
        })


@app.route('/api/neural_network_test', methods=['POST'])
def neural_network_test():
    """Test neural network creation and execution."""
    try:
        # Get GPU information
        gpu_info = get_gpu_info()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Record start time
        start_time = time.time()
        
        # Create model
        model = DemoInceptionCNN(num_classes=10)
        model.to(device)
        
        # Count parameters
        total_params = sum(p.numel() for p in model.parameters())
        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        
        # Generate synthetic test data (batch_size=4, channels=3, height=224, width=224)
        test_input = torch.randn(4, 3, 224, 224).to(device)
        
        # Perform forward pass
        model.eval()
        with torch.no_grad():
            output = model(test_input)
        
        # Calculate processing time
        processing_time = time.time() - start_time
        
        # Get memory usage if on GPU
        memory_usage = {}
        if torch.cuda.is_available():
            memory_info = torch.cuda.mem_get_info()
            memory_usage = {
                "memory_used_gb": round((memory_info[1] - memory_info[0]) / 1e9, 2),
                "memory_total_gb": round(memory_info[1] / 1e9, 2),
                "memory_used_percent": round(((memory_info[1] - memory_info[0]) / memory_info[1]) * 100, 1)
            }
        
        # Architecture information
        architecture_info = [
            {
                "layer": 1,
                "type": "Conv2d + MaxPool2d",
                "description": "Initial convolution (3→64 channels, 7x7 kernel)",
                "output_shape": "64 × H/4 × W/4"
            },
            {
                "layer": 2,
                "type": "Inception Block",
                "description": "Inception block 1 (64→128 channels)",
                "output_shape": "128 × H/4 × W/4"
            },
            {
                "layer": 3,
                "type": "Inception Block",
                "description": "Inception block 2 (128→256 channels)",
                "output_shape": "256 × H/4 × W/4"
            },
            {
                "layer": 4,
                "type": "Fully Connected",
                "description": "Adaptive pooling + classifier (256×7×7→10)",
                "output_shape": "10 classes"
            }
        ]
        
        result = {
            "success": True,
            "device_used": str(device).upper(),
            "cuda_available": torch.cuda.is_available(),
            "processing_time": round(processing_time, 3),
            "architecture": architecture_info,
            "model_stats": {
                "total_parameters": f"{total_params:,}",
                "trainable_parameters": f"{trainable_params:,}",
                "model_size_mb": round(total_params * 4 / (1024 * 1024), 2)
            },
            "test_results": {
                "input_shape": list(test_input.shape),
                "output_shape": list(output.shape),
                "forward_pass": "Success"
            },
            "memory_usage": memory_usage,
            "gpu_info": gpu_info
        }
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Neural Network Test Error: {e}")
        print(traceback.format_exc())
        return jsonify({
            "success": False,
            "error": str(e),
            "error_type": type(e).__name__
        })


if __name__ == '__main__':
    print("AI Testing Web Application - v2")
    print("=" * 40)
    
    # Check if config file exists
    if not CONFIG_PATH.exists():
        print(f"⚠️  Configuration file not found!")
        print(f"Please copy {CONFIG_TEMPLATE_PATH} to {CONFIG_PATH}")
        print("and add your OpenAI API key.")
    else:
        print("✅ Configuration file found")
    
    # Check GPU availability
    if torch.cuda.is_available():
        print(f"✅ CUDA GPU available: {torch.cuda.get_device_name()}")
    else:
        print("ℹ️  No CUDA GPU available, using CPU")
    
    print("\n🚀 Starting server...")
    print("📱 Open your browser and navigate to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 40)
    
    app.run(debug=True, host='0.0.0.0', port=5000) 