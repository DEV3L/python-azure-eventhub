import logging
import sys

from utils.env import env

default_level = env('DEFAULT_LOGGING_LEVEL', default=logging.INFO)
default_logging_format = env('DEFAULT_LOGGING_FORMAT',
                             default='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class LoggingService:
    def __init__(self, name: str, *, logging_format: str = default_logging_format, level: int = default_level):
        self.name = name
        self.logging_format = logging_format
        self.level = level

        self._logger = None

    @property
    def logger(self):
        if self._logger:
            return self._logger

        self._logger = self._build_logger()
        return self._logger

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def exception(self, message):
        self.logger.exception(message)

    def _build_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)

        sys_stdout_stream_handler = self._build_stream_handler(sys.stdout)
        logger.addHandler(sys_stdout_stream_handler)

        return logger

    def _build_stream_handler(self, stream):
        formatter = logging.Formatter(self.logging_format)

        stream_handler = logging.StreamHandler(stream)
        stream_handler.setLevel(self.level)
        stream_handler.setFormatter(formatter)

        return stream_handler
