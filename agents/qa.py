import os
from typing import Any
from ollama import Client
from core.config import config

class QAAgent:
    # TODO:  AgentFactory

    def __init__(self) -> None:
        self.client: Client = Client(host=config.get_ollama_host())
        self.model: str = config.get_local_qa_model()

    def _get_system_prompt(self) -> str:
        base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path: str = os.path.join(base_dir, "prompts", "qa_skill.md")
        
        if not os.path.exists(file_path):
            return "You are a QA Engineer. Review the code strictly."
            
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def review_code(self, coder_output: str) -> str:
        system_prompt: str = self._get_system_prompt()
        
        # DeepSeek через Ollama приймає системний промпт як перше повідомлення з роллю "system"
        messages: list[dict[str, str]] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Hey, review this code please:\n\n{coder_output}"}
        ]
        
        response: Any = self.client.chat(
            model=self.model,
            messages=messages
        )
        
        return str(response['message']['content'])