"""
Django settings for keedriver project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1-2kfp%+^+7h@d$#bj(c$7d%t+01taskh-$647e#!s3=!76_qv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "65.0.184.137",
    "43.205.194.9",
    "3.110.169.239",
    "api.keedriver.com",
    "crm.keedriver.com",
    "www.crm.keedriver.com",
    "www.api.keedriver.com",
    # "devapi.keedriver.com",
    # "www.devapi.keedriver.com",
]

CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    # 3-rd party before admin
    "dal",
    "dal_select2",
    #
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3-rd party
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "treebeard",
    "dj_rest_auth",
    "django_filters",
    "drf_spectacular",
    "import_export",
    "rangefilter",
    # apps
    "accounts.apps.AccountsConfig",
    "trips",
    "areas",
    "wallets",
    "hire_us",
    "reviews",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "keedriver.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "keedriver.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        # "default": {
        #     "ENGINE": "django.db.backends.sqlite3",
        #     "NAME": BASE_DIR / "db.sqlite3",
        # }
        # "default": {
        #     "ENGINE": "django.db.backends.postgresql",
        #     "NAME": "keedriver_dev",
        #     "USER": env("DB_USER"),
        #     "PASSWORD": env("DB_PASSWORD"),
        #     "HOST": env("DB_HOST"),
        #     "PORT": env("DB_PORT"),
        # }
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "keedriver_dev",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "localhost",
            "PORT": env("DB_PORT"),
        }
    }

if not DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASSWORD"),
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
            # 'OPTIONS': {
            #     'service': 'kee_driver_service',
            #     'passfile': '.my_pgpass',
            # },
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = BASE_DIR / "static/"
STATIC_URL = "/static/"

# Base url to serve media files
MEDIA_URL = "/media/"
# Path where media is stored
MEDIA_ROOT = BASE_DIR / "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Rest_Framework

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "accounts.backends.PasswordlessBackend",
]

REST_AUTH = {
    "LOGIN_SERIALIZER": "accounts.serializers.CustomLoginSerializer",
    "USER_DETAILS_SERIALIZER": "accounts.serializers.CustomUserDetailSerializer",
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "kee-driver-auth",
    "JWT_AUTH_REFRESH_COOKIE": "kee-driver-refresh-token",
    "JWT_AUTH_RETURN_EXPIRATION": True,
    "JWT_AUTH_HTTPONLY": False,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=2) if DEBUG else timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=3),
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "keedriver.utils.CustomPagination",
    "PAGE_SIZE": 15,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# Custom User
AUTH_USER_MODEL = "accounts.MyUser"

# Map
LOCATION_FIELD = {
    "provider.google.api": "//maps.google.com/maps/api/js?sensor=true",
    "provider.google.api_key": "AIzaSyC8Wz-5E-JkgNLy-W0L4OGUp56mqvjVcD4",
    "provider.google.api_libraries": "",
    "provider.google.map.type": "ROADMAP",
}

# API Documentation
SPECTACULAR_SETTINGS = {
    "TITLE": "Keedriver API",
    "DESCRIPTION": "Trip booking system",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
