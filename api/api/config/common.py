from os.path import join
import os
from configurations import Configuration
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

class Common(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '&fakuc1%p(l9d6$migqj^jz(ff5-k8ij#zbps5q#$win$__e+j'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'stdimage',
        'polymorphic',
        'rest_framework',
        'rest_framework.authtoken',
        'rest_framework_simplejwt',
        'phone_number.apps.PhoneNumberConfig',
        'users.apps.UsersConfig',
        'feeds.apps.FeedsConfig',
        'suggests.apps.SuggestsConfig',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'api.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'api.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': os.getenv('POSTGRES_USER'),
            'HOST': os.getenv('POSTGRES_DB'),  # set in docker-compose.yml
            'PORT': 5432,  # default postgres port
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/2.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # LOGGING = {
    #     'version': 1,
    #     'disable_existing_loggers': False,
    #     'formatters': {
    #         'simple': {
    #             'format': 'velname)s %(message)s'
    #         },
    #     },
    #     'handlers': {
    #         'console': {
    #             'level': 'INFO',
    #             'class': 'logging.StreamHandler',
    #             'formatter': 'simple'
    #         },
    #         'logstash': {
    #             'level': 'INFO',
    #             'class': 'logstash.TCPLogstashHandler',
    #             'host': 'logstash',
    #             'port': 5000,
    #             'version': 1,
    #             # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
    #             'message_type': 'django',  # 'type' field in logstash message. Default value: 'logstash'.
    #             'fqdn': False,  # Fully qualified domain name. Default value: false.
    #             'tags': ['django.request'],  # list of tags. Default: None.
    #         },
    #     },
    #     'loggers': {
    #         'django.request': {
    #             'handlers': ['logstash'],
    #             'level': 'WARNING',
    #             'propagate': True,
    #         },
    #         'django': {
    #             'handlers': ['console'],
    #             'propagate': True,
    #         },
    #     }
    # }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static')

    # Media files
    MEDIA_ROOT = join(os.path.dirname(os.path.dirname(BASE_DIR)), 'media')
    MEDIA_URL = '/media/'

    AUTH_USER_MODEL = 'users.User'

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
        'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 10)),
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
        'DEFAULT_THROTTLE_RATES': {
            'anon': '1000/day',
            'user': '300/day',
        }
    }

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(days=2),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
        'ROTATE_REFRESH_TOKENS': True,
        'BLACKLIST_AFTER_ROTATION': True,

        'AUTH_HEADER_TYPES': ('Bearer',),
        'USER_ID_FIELD': 'id',
        'USER_ID_CLAIM': 'user_id',

        'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
        'TOKEN_TYPE_CLAIM': 'token_type',

        # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
        # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
        # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    }

    CELERY_BROKER_URL = 'redis://redis:6379'
    CELERY_RESULT_BACKEND = 'redis://redis:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_BEAT_SCHEDULE = {

    }
