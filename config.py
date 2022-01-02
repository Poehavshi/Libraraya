"""
Config file with all preferences of our web application
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Config class to get config preferences by app.config.from_object(Config)
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-wil-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
