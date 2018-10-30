from flask import Flask
from config import config_options


def create_app(config_name="production"):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint,url_prefix="/api")
    return app