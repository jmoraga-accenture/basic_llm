# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Basic OpenAI API Client package.

This package provides a modular OpenAI API client with GPU testing capabilities.
It includes utilities for configuration management, GPU testing, and neural
network model implementation.
"""

from src.openai_client import OpenAIClient
from src.config_manager import ConfigManager
from src.test_relu_model import SimpleModel, create_model, generate_dummy_data, print_model_architecture
from src.gpu_utils import get_gpu_info, print_gpu_info

__all__ = [
    'OpenAIClient',
    'ConfigManager',
    'SimpleModel',
    'create_model',
    'generate_dummy_data',
    'print_model_architecture',
    'get_gpu_info',
    'print_gpu_info'
] 