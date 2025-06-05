# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Unit tests for GPU utilities.

This module contains unit tests for the GPU utility functions in the gpu_utils module.
"""

import unittest
import torch
from src.gpu_utils import get_gpu_info, print_gpu_info


class TestGPUUtils(unittest.TestCase):
    """Test cases for GPU utility functions."""

    def test_get_gpu_info(self) -> None:
        """Test GPU information retrieval."""
        info = get_gpu_info()
        
        # Check required keys
        self.assertIn("cuda_available", info)
        self.assertIn("cuda_version", info)
        self.assertIn("gpu_count", info)
        self.assertIn("gpu_info", info)
        self.assertIn("system_info", info)
        
        # Check types
        self.assertIsInstance(info["cuda_available"], bool)
        self.assertIsInstance(info["cuda_version"], str)
        self.assertIsInstance(info["gpu_count"], int)
        self.assertIsInstance(info["gpu_info"], list)
        self.assertIsInstance(info["system_info"], dict)
        
        # Check GPU info structure if CUDA is available
        if info["cuda_available"]:
            self.assertGreater(info["gpu_count"], 0)
            self.assertGreater(len(info["gpu_info"]), 0)
            for gpu in info["gpu_info"]:
                self.assertIn("name", gpu)
                self.assertIn("memory_total", gpu)
                self.assertIn("memory_free", gpu)

    def test_print_gpu_info(self) -> None:
        """Test GPU information printing."""
        # This is a visual test, but we can verify it doesn't raise exceptions
        try:
            print_gpu_info()
        except Exception as e:
            self.fail(f"print_gpu_info raised {type(e).__name__}: {e}")

    def test_cuda_availability(self) -> None:
        """Test CUDA availability matches PyTorch."""
        info = get_gpu_info()
        self.assertEqual(info["cuda_available"], torch.cuda.is_available())
        if torch.cuda.is_available():
            self.assertEqual(info["gpu_count"], torch.cuda.device_count())


if __name__ == "__main__":
    unittest.main() 