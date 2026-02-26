import sys
from colorama import Fore, Style
from agents.architect import ArchitectAgent
from agents.coder import CoderAgent
from agents.qa import QAAgent

def main() -> None:
    print(f"{Fore.CYAN}=== Initializing AI Team ==={Style.RESET_ALL}\n")
    
    # Ініціалізуємо нашу команду
    architect: ArchitectAgent = ArchitectAgent()
    coder: CoderAgent = CoderAgent()
    qa: QAAgent = QAAgent()

    # Опис твого реального завдання
    task_description: str = """
    We have a local Telegram bot for downloading torrents (written in Python). 
    We need to refactor it and add new features:
    1. The bot currently sends excessively large messages to Telegram, which causes errors or ugly UI. We need a clean way to chunk or paginate these messages.
    2. We need a new feature: when a user sends a `.torrent` file to the bot, it should parse the file, validate it, and download it to a specific local directory.
    Please design the architecture for this, focusing on OOP, strict typing, and the Single Responsibility Principle.
    """

    # STEP 1
    print(f"{Fore.MAGENTA}[Architect (Claude 4.6 Sonnet)] is drafting the architecture...{Style.RESET_ALL}")
    architecture_plan: str = architect.draft(task_description)
    print(f"{Fore.MAGENTA}--- Architecture Plan ---{Style.RESET_ALL}")
    print(architecture_plan[:500] + "...\n[TRUNCATED FOR READABILITY]\n")

    # STEP :
    print(f"{Fore.BLUE}[Coder (Gemini 3.0 Pro)] is writing the code...{Style.RESET_ALL}")
    draft_code: str = coder.write_code(architecture_plan)
    print(f"{Fore.BLUE}--- Draft Code ---{Style.RESET_ALL}")
    print(draft_code[:500] + "...\n[TRUNCATED FOR READABILITY]\n")

    # STEP 3: QA (DeepSeek)
    print(f"{Fore.YELLOW}[QA (DeepSeek R1)] is reviewing the code...{Style.RESET_ALL}")
    review_feedback: str = qa.review_code(draft_code)
    print(f"{Fore.YELLOW}--- QA Review ---{Style.RESET_ALL}")
    print(review_feedback)
    
    print(f"\n{Fore.GREEN}=== Workflow Complete ==={Style.RESET_ALL}")

if __name__ == "__main__":
    main()