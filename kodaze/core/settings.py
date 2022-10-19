"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os

from django.conf import settings
from celery.schedules import crontab

from dotenv import load_dotenv, find_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(find_dotenv())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
__PRODUCTION__ = True

# SECURITY WARNING: don't run with debug turned on in production!
if __PRODUCTION__ == True:
    DEBUG = False
else:
    DEBUG = True

if __PRODUCTION__ == True:
    ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(',')
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

if __PRODUCTION__ == False:
    INTERNAL_IPS = [
        "127.0.0.1",
        "localhost"
    ]


CSRF_TRUSTED_ORIGINS = [
    'https://dev.kodaze.com'
]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party libraries
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_beat',
    'django_celery_results',
    'django_extensions',
    'django_filters',
    'dbbackup',
    "corsheaders",
    "debug_toolbar",
    "sphinx_view",

    # apps
    'account.apps.AccountConfig',
    'company.apps.CompanyConfig',
    'cashbox.apps.CashboxConfig',
    'transfer.apps.TransferConfig',
    'income_expense.apps.IncomeExpenseConfig',
    'holiday.apps.HolidayConfig',
    'salary.apps.SalaryConfig',
    'warehouse.apps.WarehouseConfig',
    'product.apps.ProductConfig',
    'contract.apps.ContractConfig',
    'services.apps.ServicesConfig',
    'backup_restore.apps.BackupRestoreConfig',
    'update.apps.UpdateConfig',
    'task_manager.apps.TaskManagerConfig'
]


DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
backup_adress = os.path.join(BASE_DIR, 'backup')
DBBACKUP_STORAGE_OPTIONS = {'location': backup_adress}

SIMPLE_JWT = {
    # When set to True, if a refresh token is submitted to the TokenRefreshView, a new refresh token will be returned along with the new access token.
    'ROTATE_REFRESH_TOKENS': True,
    # refresh tokens submitted to the TokenRefreshView to be added to the blacklist
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',  # TWO types either HMAC  or RSA for HMAC 'HS256', 'HS384', 'HS512: SIGNING_KEY setting will be used as both the signing key and the verifying key.  asymmetric RSA RS256', 'RS384', 'RS512' SIGNING_KEY setting must be set to a string that contains an RSA private key. Likewise, the VERIFYING_KEY
    'SIGNING_KEY': settings.SECRET_KEY,  # content of generated tokens.
    # The verifying key which is used to verify the content of generated tokens
    'VERIFYING_KEY': None,
    # The audience claim to be included in generated tokens and/or validated in decoded tokens
    'AUDIENCE': None,
    'ISSUER': None,  # ssuer claim to be included in generated tokens

    # Authorization: Bearer <token> ('Bearer', 'JWT')
    'AUTH_HEADER_TYPES': ('Bearer',),
    # The database field from the user model that will be included in generated tokens to identify users.
    'USER_ID_FIELD': 'id',
    # value of 'user_id' would mean generated tokens include a “user_id” claim that contains the user’s identifier.
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # The claim ad that is used to store a token’s type
    'TOKEN_TYPE_CLAIM': 'token_type',

    # The claim ad that is used to store a token’s unique identifier.
    'JTI_CLAIM': 'jti',
    # which specifies how long access tokens are valid
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    # how long refresh tokens are valid.
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

AUTH_USER_MODEL = 'account.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if __PRODUCTION__ == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['POSTGRES_DB'],
            'USER': os.environ['POSTGRES_USER'],
            'PASSWORD': os.environ['POSTGRES_PASSWORD'],
            'HOST': 'db',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'core.password_validator.UppercaseValidator',
#     },
#     {
#         'NAME': 'core.password_validator.NumberValidator',
#     },
#     {
#         'NAME': 'core.password_validator.CustomUserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'core.password_validator.CustomCommonPasswordValidator',
#     },
#     {
#         'NAME': 'core.password_validator.SymbolValidator',
#     },
#     {
#         'NAME': 'core.password_validator.MinimumLengthValidator',
#     }
# ]

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

DATE_FORMAT=['%d-%m-%Y']

USE_L10N = False

USE_TZ = True

# CORS conf
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
if __PRODUCTION__:
    STATIC_ROOT = '/static/'
else:
    STATIC_ROOT = 'kodaze/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR)

DOCS_URL = '/docs/'
DOCS_ROOT = os.path.join(BASE_DIR, 'docs', '_build')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ),
    'DATE_INPUT_FORMATS': ["%d-%m-%Y", ],
    'DATETIME_FORMAT':  "%d-%m-%Y %H:%M:%S",
    'DATE_FORMAT':  "%d-%m-%Y",
    'DATETIME_INPUT_FORMATS':  ["%d-%m-%Y %H:%M:%S", ],

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

# CELERY_CACHE_BACKEND = 'default'
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'alliance_cache_table',
#     }
# }
CACHE_TTL = 60 * 15
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:ENA7eWv7s58AZCDm4MtyKVPe8oNd2690@redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "kodaze_cache_table"
    }
}

CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Baku'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
