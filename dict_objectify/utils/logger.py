import logging
import sys


def configure_logger(logger: logging.Logger) -> None:
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(name)-12s: %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    stdout_handler.setLevel(logging.DEBUG)

    def stdout_handler_filter(rec: logging.LogRecord):
        return False if rec.levelno >= logging.WARNING else True

    stdout_handler.filter = stdout_handler_filter

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(formatter)
    stderr_handler.setLevel(logging.WARNING)

    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)
    logger.setLevel(level=logging.INFO)  # type: ignore


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    configure_logger(logger)
    return logger
