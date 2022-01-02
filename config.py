"""
Config file with all preferences of our web application
"""

import os


class Config:
    """
    Config class to get config preferences by app.config.from_object(Config)
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-wil-never-guess'
