import sys
import logging
import argparse
from core.logger import setup_logger
from core.monitor import run_diagnostics
from core.config import config
from typing import Any

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="AI Orchestrator")
    parser.add_argument("--log", action="store_true", help="Enable writing logs to a file")
    args: argparse.Namespace = parser.parse_args()

    run_id: int = setup_logger(enable_file_log=args.log)
    
    if args.log:
        logging.warning(f"Starting orchestrator run: {run_id}")
    
    required_models: list[str] = [config.get_local_qa_model()]
    
    required_config: dict[str, Any] = {
        "ANTHROPIC_API_KEY": config.get_anthropic_api_key(),
        "GEMINI_API_KEY": config.get_gemini_api_key(),
        "OLLAMA_HOST": config.get_ollama_host()
    }
    
    diagnostics_passed: bool = run_diagnostics(
        required_models, 
        required_config, 
        config.get_ollama_host()
    )
    
    if not diagnostics_passed:
        logging.error("System diagnostics failed. Exiting.")
        sys.exit(1)
        
    if args.log:
        logging.warning("System diagnostics passed. Ready to initialize agents.")
        
    print("All systems GO. Ready to initialize agents.")

if __name__ == "__main__":
    main()