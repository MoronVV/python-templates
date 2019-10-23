import logging

from flask import Blueprint

logger = logging.getLogger(__name__)
views = Blueprint('views', __name__)


@views.route('/')
def main():
    logger.debug("Hello, world")
    return "Hello, world"
