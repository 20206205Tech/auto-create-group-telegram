from environs import Env
from loguru import logger

env = Env()
logger.info("Loading environment variables...")


TELEGRAM_API_ID = env.str("TELEGRAM_API_ID")
TELEGRAM_API_HASH = env.str("TELEGRAM_API_HASH")
TELEGRAM_SESSION = env.str("TELEGRAM_SESSION")

