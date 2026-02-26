import os
from google import genai
from google.genai import types
from core.config import config

class CoderAgent:
    # TODO: later will improve as factory + role maneger

    def __init__(self) -> None:
        self.client: genai.Client = genai.Client(api_key=config.get_gemini_api_key())
        self.model: str = config.get_gemini_model()

    def _get_system_prompt(self) -> str:
        base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path: str = os.path.join(base_dir, "prompts", "coder_skill.md")
        
        if not os.path.exists(file_path):
            return "You are an expert Senior Developer. Write concise, clean code based on the provided architecture."
            
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def write_code(self, architecture_plan: str) -> str:
        system_prompt: str = self._get_system_prompt()
        
        # Використовуємо GenerateContentConfig для передачі системних інструкцій
        generation_config: types.GenerateContentConfig = types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.2  # Низька температура для більшої детермінованості коду
        )
        
        response: types.GenerateContentResponse = self.client.models.generate_content(
            model=self.model,
            contents=architecture_plan,
            config=generation_config
        )
        
        return str(response.text)