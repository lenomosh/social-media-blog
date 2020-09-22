import os
from instance.config import config_options
from flask import Flask
from app.db import db
from flask_cors import CORS


def create_app(config_name='dev'):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # CORS(app)
    app.config.from_object(config_options[config_name])
    db.init_app(app)
    from app.api import api
    app.register_blueprint(api, url_prefix='/api')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
