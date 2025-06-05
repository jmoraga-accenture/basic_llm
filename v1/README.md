# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Basic OpenAI API Client with GPU Testing

A modular OpenAI API client with GPU testing capabilities, built with PyTorch and following Google's Python style guide.

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd basic_llm
   ```

2. Set up the environment:
   ```bash
   mamba env create -f environment.yml
   mamba activate ptorchy
   ```

3. Configure the API:
   ```bash
   cp config/config.json.template config/config.json
   # Edit config.json with your OpenAI API key
   ```

4. Run the tests:
   ```bash
   python test_gpu.py  # Test GPU functionality
   python main.py      # Test OpenAI API
   ```

## Features

- Modular OpenAI API client
- GPU testing and monitoring
- Neural network model implementation
- Configuration management
- Comprehensive error handling
- Type hints and documentation
- Google style guide compliance

## Requirements

- Python 3.8+
- PyTorch with CUDA support
- OpenAI API key
- Mamba/Conda environment manager

## Documentation

- [Quick Start Guide](README.md) (this file)
- [Detailed Specifications](SPECIFICATIONS.md)
- [Code Style Guide](docs/STYLE_GUIDE.md)

## License

Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

All rights reserved.