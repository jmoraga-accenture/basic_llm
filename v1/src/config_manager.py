import json
import os
from pathlib import Path
from typing import Dict, Any

class ConfigManager:
    def __init__(self, config_path: str = "config/config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self.load_config()

    def load_config(self) -> None:
        """Load configuration from the JSON file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(
                f"Configuration file not found at {self.config_path}. "
                "Please copy config.json.template to config.json and add your API key."
            )

        with open(self.config_path, 'r') as f:
            self.config = json.load(f)

        self._validate_config()

    def _validate_config(self) -> None:
        """Validate the configuration structure and required fields."""
        required_fields = {
            'openai': {
                'api_key': str,
                'model': str,
                'temperature': (int, float),
                'max_tokens': int
            }
        }

        if 'openai' not in self.config:
            raise ValueError("Missing 'openai' section in configuration")

        for field, field_type in required_fields['openai'].items():
            if field not in self.config['openai']:
                raise ValueError(f"Missing required field '{field}' in OpenAI configuration")
            
            if not isinstance(self.config['openai'][field], field_type):
                raise ValueError(f"Invalid type for field '{field}' in OpenAI configuration")

    def get_openai_config(self) -> Dict[str, Any]:
        """Get the OpenAI configuration section."""
        return self.config['openai'] 