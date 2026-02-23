import logging
import time

def setup_logger():
    run_id = int(time.time())
    log_filename = f'orchestrator_{run_id}.log'
    
    logging.basicConfig(
        filename=log_filename,
        level=logging.WARNING,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    return run_id