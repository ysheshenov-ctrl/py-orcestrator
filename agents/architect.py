import os
from typing import Any
from anthropic import Anthropic
from core.config import config

class ArchitectAgent:
    def __init__(self) -> None:
        self.client: Anthropic = Anthropic(api_key=config.get_anthropic_api_key())
        self.model: str = config.get_anthropic_model()

    def _get_system_prompt(self) -> str:
        base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path: str = os.path.join(base_dir, "prompts", "architect_skill.md")
        
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def draft(self, user_request: str) -> str:
        system_prompt: str = self._get_system_prompt()
        
        response: Any = self.client.messages.create(
            model=self.model,
            max_tokens=16000,
            system=system_prompt,
            thinking=config.get_claude_thinking(),
            output_config=config.get_claude_output_config(),
            messages=[{"role": "user", "content": user_request}]
        )
        
        # Шукаємо саме текстовий блок, ігноруючи ThinkingBlock
        for block in response.content:
            if block.type == 'text':
                return str(block.text)
                
        return "Error: No text block found in response."