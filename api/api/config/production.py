import os
from .common import Common


class Production(Common):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')