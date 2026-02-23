import os
import logging
import requests
import ollama
from colorama import Fore, Style
from typing import Any

def verify_service(host_url: str) -> bool:
    try:
        response: requests.Response = requests.get(host_url, timeout=2)
        is_active: bool = response.status_code == 200
        if not is_active:
            logging.error("Ollama service responded with non-200 status.")
        return is_active
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to Ollama daemon: {e}")
        return False

def verify_models(required_models: list[str]) -> bool:
    try:
        response = ollama.list()
        available: list[str] = [m.model for m in response.models]
        
        for required in required_models:
            if required not in available:
                logging.error(f"Required model missing: {required}. Found models: {available}")
                return False
                
        return True
    except Exception as e:
        logging.error(f"Failed to fetch models from Ollama: {e}")
        return False
    
def verify_environment(config_vars: dict[str, Any]) -> bool:
    for name, value in config_vars.items():
        if not value:
            logging.error(f"Missing required configuration: {name}")
            return False
    return True

def run_diagnostics(required_models: list[str], config_vars: dict[str, Any], ollama_host: str) -> bool:
    print(f"{Fore.CYAN}System Diagnostics:{Style.RESET_ALL}")
    
    service_status: bool = verify_service(ollama_host)
    if service_status:
        print(f"Ollama Daemon: {Fore.GREEN}OK{Style.RESET_ALL}")
    else:
        print(f"Ollama Daemon: {Fore.RED}FAIL{Style.RESET_ALL}")
    
    models_status: bool = verify_models(required_models)
    if models_status:
        print(f"Local Models: {Fore.GREEN}OK{Style.RESET_ALL}")
    else:
        print(f"Local Models: {Fore.RED}FAIL{Style.RESET_ALL}")
    
    env_status: bool = verify_environment(config_vars)
    if env_status:
        print(f"API Keys: {Fore.GREEN}OK{Style.RESET_ALL}")
    else:
        print(f"API Keys: {Fore.RED}FAIL{Style.RESET_ALL}")
    
    return service_status and models_status and env_status