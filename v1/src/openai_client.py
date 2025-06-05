from typing import Dict, Any, Optional
from openai import OpenAI
from .config_manager import ConfigManager

class OpenAIClient:
    def __init__(self, config_path: str = "config/config.json"):
        """Initialize the OpenAI client with configuration."""
        self.config_manager = ConfigManager(config_path)
        self.client = self._initialize_client()

    def _initialize_client(self) -> OpenAI:
        """Initialize the OpenAI client with API key."""
        config = self.config_manager.get_openai_config()
        return OpenAI(api_key=config['api_key'])

    def query(
        self,
        prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Send a query to the OpenAI API and return the response.

        Args:
            prompt: The input prompt to send to the model
            temperature: Optional temperature override (0.0 to 1.0)
            max_tokens: Optional max tokens override

        Returns:
            The model's response as a string
        """
        config = self.config_manager.get_openai_config()
        
        # Use provided parameters or fall back to config defaults
        temperature = temperature if temperature is not None else config['temperature']
        max_tokens = max_tokens if max_tokens is not None else config['max_tokens']

        try:
            response = self.client.chat.completions.create(
                model=config['model'],
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error querying OpenAI API: {str(e)}") 