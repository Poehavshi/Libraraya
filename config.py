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

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ["sotnikoarkady1@gmail.com"]

    POSTS_PER_PAGE = 25
