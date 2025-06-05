# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Test configuration and fixtures.

This module provides pytest fixtures and configuration for the test suite.
"""

import pytest
import torch
from src.test_relu_model import SimpleModel


@pytest.fixture
def model() -> SimpleModel:
    """Create a SimpleModel instance for testing.
    
    Returns:
        SimpleModel: A fresh model instance for each test.
    """
    return SimpleModel()


@pytest.fixture
def device() -> torch.device:
    """Get the appropriate device for testing.
    
    Returns:
        torch.device: The device to use for testing (CUDA if available, else CPU).
    """
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


@pytest.fixture
def batch_size() -> int:
    """Get the batch size for testing.
    
    Returns:
        int: The batch size to use in tests.
    """
    return 32


@pytest.fixture
def input_size() -> int:
    """Get the input size for testing.
    
    Returns:
        int: The input size to use in tests.
    """
    return 784


@pytest.fixture
def output_size() -> int:
    """Get the output size for testing.
    
    Returns:
        int: The output size to use in tests.
    """
    return 10 