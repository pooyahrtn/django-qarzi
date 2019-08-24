import os
from .common import Common


class Production(Common):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
