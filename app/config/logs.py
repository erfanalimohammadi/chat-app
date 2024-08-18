import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
from pathlib import Path
from .config import BASE_DIR, get_settings

settings = get_settings()

log_path = Path(BASE_DIR / settings.log_file_path)
try:
    log_path.parent.mkdir(parents=True, exist_ok=True)
except Exception as e:
    print(f"Error creating log directory: {e}")
    raise

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

try:
    logging.basicConfig(
        level=settings.log_level.upper(), 
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(),  
            RotatingFileHandler(
                log_path,
                maxBytes=settings.log_max_bytes,
                backupCount=settings.log_backup_count,
            ), 
        ],
    )
except Exception as e:
    print(f"Error setting up logging: {e}")
    raise

logging.getLogger("passlib").setLevel(logging.ERROR)

logger: Logger = logging.getLogger("ChatApp")

logger.info("Logging configuration is set up.")


def get_logger(name: str) -> Logger:
    return logging.getLogger(name)
