# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Neural network model for GPU testing and verification.

This module provides a simple fully connected neural network model for testing
GPU functionality and PyTorch operations. It includes utilities for model
creation, architecture visualization, and performance testing.
"""

from typing import Dict, Any, Optional, List
import torch
import torch.nn as nn
import torch.nn.functional as F


class SimpleModel(nn.Module):
    """A simple fully connected neural network model.

    This model implements a basic feed-forward neural network with configurable
    layer sizes and ReLU activation functions. It's designed for testing GPU
    functionality and PyTorch operations.

    Attributes:
        fc1: First fully connected layer.
        fc2: Second fully connected layer.
        fc3: Output layer.
    """

    def __init__(
        self,
        input_size: int = 784,
        hidden_size: int = 128,
        num_classes: int = 10
    ) -> None:
        """Initialize the model.

        Args:
            input_size: Size of input features. Defaults to 784 (MNIST-like).
            hidden_size: Size of hidden layers. Defaults to 128.
            num_classes: Number of output classes. Defaults to 10.
        """
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass of the model.

        Args:
            x: Input tensor of shape (batch_size, input_size).

        Returns:
            Output tensor of shape (batch_size, num_classes).
        """
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def get_architecture_info(self) -> Dict[str, Any]:
        """Get detailed information about the model's architecture.

        Returns:
            Dictionary containing architecture information including layer
            configurations, parameter counts, and activation functions.
        """
        total_params = sum(p.numel() for p in self.parameters())
        trainable_params = sum(p.numel() for p in self.parameters() if p.requires_grad)

        architecture = {
            "input_size": self.fc1.in_features,
            "hidden_size": self.fc1.out_features,
            "output_size": self.fc3.out_features,
            "total_parameters": total_params,
            "trainable_parameters": trainable_params,
            "layers": [
                {
                    "name": "fc1",
                    "type": "Linear",
                    "in_features": self.fc1.in_features,
                    "out_features": self.fc1.out_features,
                    "activation": "ReLU"
                },
                {
                    "name": "fc2",
                    "type": "Linear",
                    "in_features": self.fc2.in_features,
                    "out_features": self.fc2.out_features,
                    "activation": "ReLU"
                },
                {
                    "name": "fc3",
                    "type": "Linear",
                    "in_features": self.fc3.in_features,
                    "out_features": self.fc3.out_features,
                    "activation": "None"
                }
            ]
        }
        return architecture


def create_model(device: torch.device) -> SimpleModel:
    """Create and initialize a model on the specified device.

    Args:
        device: Device to place the model on (CPU or GPU).

    Returns:
        Initialized model placed on the specified device.
    """
    model = SimpleModel()
    return model.to(device)


def generate_dummy_data(
    batch_size: int = 32,
    input_size: int = 784
) -> torch.Tensor:
    """Generate dummy data for testing.

    Args:
        batch_size: Number of samples to generate. Defaults to 32.
        input_size: Size of each input sample. Defaults to 784.

    Returns:
        Tensor of shape (batch_size, input_size) containing random data.
    """
    return torch.randn(batch_size, input_size)


def print_model_architecture(model: SimpleModel) -> None:
    """Print a detailed visualization of the model's architecture.

    Args:
        model: The model to visualize.
    """
    arch_info = model.get_architecture_info()

    print("\n=== Model Architecture ===")
    print(f"Input Size: {arch_info['input_size']}")
    print(f"Hidden Size: {arch_info['hidden_size']}")
    print(f"Output Size: {arch_info['output_size']}")
    print(f"\nTotal Parameters: {arch_info['total_parameters']:,}")
    print(f"Trainable Parameters: {arch_info['trainable_parameters']:,}")

    print("\nLayer Structure:")
    print("-" * 60)
    print(f"{'Layer Name':<10} {'Type':<10} {'Input Size':<12} {'Output Size':<12} {'Activation':<10}")
    print("-" * 60)

    for layer in arch_info['layers']:
        print(
            f"{layer['name']:<10} {layer['type']:<10} "
            f"{layer['in_features']:<12} {layer['out_features']:<12} "
            f"{layer['activation']:<10}"
        )

    print("-" * 60)
    print("\nData Flow:")
    print(f"Input ({arch_info['input_size']}) →")
    print(f"  FC1 + ReLU → ({arch_info['hidden_size']}) →")
    print(f"  FC2 + ReLU → ({arch_info['hidden_size']}) →")
    print(f"  FC3 → Output ({arch_info['output_size']})")
    print("=" * 60) 