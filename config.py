import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class TestingConfig(BaseConfig):
    # secret key enables flask.session, which lets flask
    # remember data from one request to another via a signed cookie.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sirius black'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # suppress annoying msg
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4 # number of password hashing rounds can be
        # safely reduced when testing, to reduce test execution time.
    WTF_CSRF_ENABLED = False # CSRF tokens in forms must be disabled for tests to run.

class DevelopmentConfig(TestingConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    WTF_CSRF_ENABLED = True

class ProductionConfig(DevelopmentConfig):
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['mwroffo@gmail.com']
