import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'dev'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@localhost/pitch.'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:root@localhost/pitching_app'
    # DATABASE_URL = 'postgresql+psycopg2://moringa:root@localhost/pitching_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/storage/profile_pictures'
    JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProdConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']


config_options = {
    'dev': DevConfig,
    'prod': ProdConfig
}
