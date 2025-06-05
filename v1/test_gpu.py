# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Test script for GPU functionality and model performance.

This script tests various aspects of GPU functionality including:
- GPU availability and CUDA support
- Basic tensor operations
- Model creation and placement
- Performance measurements
"""

from src.gpu_utils import print_gpu_info
from src.test_relu_model import create_model, generate_dummy_data, print_model_architecture
import torch
import time


def test_gpu_functionality() -> None:
    """Test basic GPU functionality with a simple tensor operation.

    This function:
        1. Displays GPU information
        2. Creates random tensors on GPU
        3. Performs matrix multiplication
        4. Measures and displays performance
    """
    print_gpu_info()

    if torch.cuda.is_available():
        print("\nTesting GPU with a simple tensor operation...")

        # Create a tensor on GPU
        x = torch.rand(1000, 1000).cuda()
        y = torch.rand(1000, 1000).cuda()

        # Perform a matrix multiplication
        start_event = torch.cuda.Event(enable_timing=True)
        end_event = torch.cuda.Event(enable_timing=True)

        start_event.record()
        z = torch.matmul(x, y)
        end_event.record()

        # Wait for GPU operations to complete
        torch.cuda.synchronize()

        # Calculate elapsed time
        elapsed_time = start_event.elapsed_time(end_event)
        print(f"Matrix multiplication completed in {elapsed_time:.2f} ms")

        # Verify the result
        print(f"Result tensor shape: {z.shape}")
        print(f"Result tensor device: {z.device}")
        print("GPU test completed successfully!")
    else:
        print("\nNo GPU available for testing.")


def test_model() -> None:
    """Test model creation and forward pass with dummy data.

    This function:
        1. Creates and initializes the model
        2. Displays model architecture
        3. Generates and processes dummy data
        4. Measures forward pass performance
        5. Displays results and statistics
    """
    print("\n=== Testing Model ===")

    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    try:
        # Create model
        print("Creating model...")
        model = create_model(device)
        print(f"Model created successfully on {next(model.parameters()).device}")

        # Print model architecture
        print_model_architecture(model)

        # Generate dummy data
        print("\nGenerating dummy data...")
        batch_size = 32
        dummy_data = generate_dummy_data(batch_size).to(device)
        print(f"Dummy data shape: {dummy_data.shape}")

        # Test forward pass
        print("\nTesting forward pass...")
        start_time = time.time()
        with torch.no_grad():
            output = model(dummy_data)
        end_time = time.time()

        # Print results
        print(f"Forward pass completed in {(end_time - start_time)*1000:.2f} ms")
        print(f"Output shape: {output.shape}")
        print(f"Output device: {output.device}")

        # Test model parameters
        total_params = sum(p.numel() for p in model.parameters())
        print(f"\nTotal model parameters: {total_params:,}")

        print("\nModel test completed successfully!")

    except Exception as e:
        print(f"Error during model test: {str(e)}")
        raise


def main() -> None:
    """Main function to run all tests."""
    test_gpu_functionality()
    test_model()


if __name__ == "__main__":
    main() 