import os
from dotenv import load_dotenv

class Config:
    def __init__(self) -> None:
        load_dotenv()
        
        self._anthropic_model: str = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
        self._gemini_model: str = os.environ.get("GEMINI_MODEL", "gemini-3-pro-preview")
        self._local_qa_model: str = os.environ.get("LOCAL_QA_MODEL", "deepseek-r1:14b")
        
        self._anthropic_api_key: str | None = os.environ.get("ANTHROPIC_API_KEY")
        self._gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY")
        
        self._ollama_host: str = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")

    def get_anthropic_model(self) -> str:
        return self._anthropic_model

    def get_gemini_model(self) -> str:
        return self._gemini_model

    def get_local_qa_model(self) -> str:
        return self._local_qa_model

    def get_anthropic_api_key(self) -> str | None:
        return self._anthropic_api_key

    def get_gemini_api_key(self) -> str | None:
        return self._gemini_api_key

    def get_ollama_host(self) -> str:
        return self._ollama_host

    def get_claude_thinking(self) -> dict[str, str]:
        # TODO: move to .env
        return {"type": "adaptive"}

    def get_claude_output_config(self) -> dict[str, str]:
        # TODO: move to .env
        return {"effort": "medium"}

config = Config()