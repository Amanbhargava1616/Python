import logging, os
from typing import Optional
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


class Logger:

    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def __init__(
        self,
        logger_name: str,
        file_name: Optional[str] = None,
    ):

        self._logger = logging.getLogger(logger_name)

        if self._logger.hasHandlers():
            self._logger.handlers.clear()

        LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO").upper()
        log_level = getattr(logging, LOGGING_LEVEL, logging.INFO)
        self._logger.setLevel(log_level)

        if not os.path.exists("logs"):
            os.makedirs("logs")

        if not file_name:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"./logs/log_file_{timestamp}.log"
        else:
            file_name = f"./logs/log_file_{file_name}.log"

        file_handler = logging.FileHandler(filename=file_name, mode="w", encoding="UTF-8")
        file_handler.setFormatter(logging.Formatter(self.LOG_FORMAT))

        terminal_handler = logging.StreamHandler()
        terminal_handler.setFormatter(logging.Formatter(self.LOG_FORMAT))

        self._logger.addHandler(file_handler)
        self._logger.addHandler(terminal_handler)

        self._logger.propagate = False

        self._logger.info(f"Logger {logger_name} is created.")

    def get_logger(self):
        return self._logger


if __name__ == "__main__":
    logger_object = Logger(logger_name=__name__, file_name="logger_module")
