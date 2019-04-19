import os
from flask import Flask
from apis.v1 import api_v1
from settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name =  os.getenv('FLASK_CONFIG', 'development')

    app = Flask('DieforAchievements')
    app.config.from_object(config[config_name])

    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api_v1, url_prefix='/api/v1')
