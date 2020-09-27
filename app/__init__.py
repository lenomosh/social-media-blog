from instance.config import config_options
from flask import Flask
from app.db import db
from flask_cors import CORS
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
photos = UploadSet('photos', IMAGES)
jwt = JWTManager()
migrate = Migrate()

def create_app(config_name='dev'):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config_options[config_name])
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)
    from app.api import api
    app.register_blueprint(api, url_prefix='/api')
    configure_uploads(app, photos)
    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/api/auth/v1.0')
    return app
