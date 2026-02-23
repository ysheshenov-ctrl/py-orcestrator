import logging
import time

def setup_logger(enable_file_log: bool = False) -> int:
    run_id: int = int(time.time())
    
    if enable_file_log:
        log_filename: str = f"orchestrator_{run_id}.log"
        logging.basicConfig(
            filename=log_filename,
            level=logging.WARNING,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
    else:
        logging.basicConfig(
            level=logging.WARNING,
            format="%(levelname)s: %(message)s"
        )
        
    return run_id