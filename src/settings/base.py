"""
All settings should be placed in here and overridden in specific env
config files (dev.py, test.py, and prod.py)
"""
import os
from os.path import dirname, abspath

SRC_DIR = dirname(dirname(abspath(__file__)))

PROJECT_ROOT = dirname(SRC_DIR)

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = False

SECRET_KEY = ''

SESSION_COOKIE_NAME = 'flask-seed'
