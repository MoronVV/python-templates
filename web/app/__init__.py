"""
Flask app
"""
from flask import Flask

from app import logger
# from app.extensions import extension
from app.views import views

# logger
logger.init()


def create_app(config='config.default'):
    # init flask
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(views)
    app.config.from_object(config)
    # to work with local configs create instance/config.py
    app.config.from_pyfile('config.py', silent=True)

    # init extensions
    # extension.init_app(app)

    return app
