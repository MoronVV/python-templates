import logging.handlers
import os
from pathlib import Path


def init(name: str) -> None:
    service_name = os.getenv('SERVICE', 'undefined')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        f"%(asctime)s.%(msecs)03dZ [{service_name}] %(levelname)s: %(message)s",
        "%Y-%m-%dT%H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if os.getenv("IN_DOCKER"):
        log_path = Path(f"/var/log/{service_name}.log")
        rotating_handler = logging.handlers.TimedRotatingFileHandler(
            log_path, when='midnight')
        rotating_handler.setLevel(logging.DEBUG)
        rotating_handler.setFormatter(formatter)
        logger.addHandler(rotating_handler)
