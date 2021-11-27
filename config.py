'''
App config
'''
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''Base config'''
    FLASK_ENV = "development"
    FLASK_DEBUG = 1
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/data/app.db"
    SQLALCHEMY_ECHO = 1
    SQLALCHEMY_TRACK_MODIFICATIONS = False
