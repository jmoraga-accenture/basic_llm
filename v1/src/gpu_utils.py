# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""GPU and CUDA utilities for testing and monitoring.

This module provides utilities for checking GPU availability, retrieving CUDA
information, and monitoring GPU performance. It includes functions for
displaying detailed system and GPU specifications.
"""

from typing import Dict, Any, List
import torch
import platform


def get_gpu_info() -> Dict[str, Any]:
    """Get detailed information about GPU and CUDA availability.

    Returns:
        Dictionary containing:
            - CUDA availability status
            - CUDA version
            - Number of GPUs
            - Detailed GPU information
            - System information
    """
    info = {
        "cuda_available": torch.cuda.is_available(),
        "cuda_version": torch.version.cuda if torch.cuda.is_available() else "N/A",
        "gpu_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
        "gpu_devices": [],
        "system_info": {
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "pytorch_version": torch.__version__
        }
    }

    if info["cuda_available"]:
        for i in range(info["gpu_count"]):
            gpu_info = {
                "name": torch.cuda.get_device_name(i),
                "memory_total": f"{torch.cuda.get_device_properties(i).total_memory / 1024**3:.2f} GB",
                "memory_free": f"{torch.cuda.memory_reserved(i) / 1024**3:.2f} GB"
            }
            info["gpu_devices"].append(gpu_info)

    return info


def print_gpu_info() -> None:
    """Print formatted GPU and CUDA information.

    This function displays a comprehensive overview of the system's GPU
    capabilities, including:
        - CUDA availability and version
        - Number of available GPUs
        - Detailed specifications for each GPU
        - System information
    """
    info = get_gpu_info()

    print("\n=== GPU and CUDA Information ===")
    print(f"CUDA Available: {info['cuda_available']}")
    if info['cuda_available']:
        print(f"CUDA Version: {info['cuda_version']}")
        print(f"Number of GPUs: {info['gpu_count']}")

        for i, gpu in enumerate(info['gpu_devices']):
            print(f"\nGPU {i}:")
            print(f"  Name: {gpu['name']}")
            print(f"  Total Memory: {gpu['memory_total']}")
            print(f"  Free Memory: {gpu['memory_free']}")
    else:
        print("No CUDA-capable GPU found")

    print("\n=== System Information ===")
    print(f"Platform: {info['system_info']['platform']}")
    print(f"Python Version: {info['system_info']['python_version']}")
    print(f"PyTorch Version: {info['system_info']['pytorch_version']}")
    print("=" * 30) 