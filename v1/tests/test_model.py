# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Unit tests for the neural network model.

This module contains unit tests for the SimpleModel class and related functions
in the test_relu_model module.
"""

import unittest
import torch
from src.test_relu_model import SimpleModel, create_model, generate_dummy_data


class TestSimpleModel(unittest.TestCase):
    """Test cases for the SimpleModel class."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.model = SimpleModel()
        self.batch_size = 32
        self.input_size = 784
        self.output_size = 10

    def test_model_creation(self) -> None:
        """Test model creation and initialization."""
        self.assertIsInstance(self.model, SimpleModel)
        self.assertEqual(self.model.input_size, self.input_size)
        self.assertEqual(self.model.output_size, self.output_size)

    def test_forward_pass(self) -> None:
        """Test forward pass through the model."""
        x = torch.randn(self.batch_size, self.input_size)
        output = self.model(x)
        self.assertEqual(output.shape, (self.batch_size, self.output_size))

    def test_device_placement(self) -> None:
        """Test model placement on available device."""
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)
        self.assertEqual(next(self.model.parameters()).device, device)

    def test_parameter_count(self) -> None:
        """Test model parameter counting."""
        total_params = sum(p.numel() for p in self.model.parameters())
        self.assertGreater(total_params, 0)


class TestModelFunctions(unittest.TestCase):
    """Test cases for model-related functions."""

    def test_create_model(self) -> None:
        """Test model creation function."""
        model = create_model()
        self.assertIsInstance(model, SimpleModel)

    def test_generate_dummy_data(self) -> None:
        """Test dummy data generation."""
        batch_size = 32
        x, y = generate_dummy_data(batch_size)
        self.assertEqual(x.shape, (batch_size, 784))
        self.assertEqual(y.shape, (batch_size, 10))


if __name__ == "__main__":
    unittest.main() 