import json
import logging.config
import os
from pathlib import Path
from secrets import token_urlsafe

import dj_database_url
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY", default=token_urlsafe(32))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Installed Apps
    "crispy_forms",
    "crispy_bootstrap5",
    "social_django",
    "rest_framework",
    "rest_framework_api_key",
    "users",
    "website",
    "social",
    "api",
    "storages",
]


# Django Sites

SITE_ID = 1


#  Rest Framework Settings

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "users.utils.apikey_auth.UserHasAPIKey",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "users.utils.apikey_auth.APIKeyAuthentication",
    ],
}

API_KEY_CUSTOM_HEADER = "HTTP_X_API_KEY"


# Middleware Configuration

MIDDLEWARE = [
    "event_manager.middlewares.redirect_middleware.WwwRedirectMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "event_manager.urls"

CORS_ALLOW_ALL_ORIGINS = True

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_AGE = 1209600  # Two weeks, in seconds
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True


# Templates Settings

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

WSGI_APPLICATION = "event_manager.wsgi.application"


# Database Settings
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=config(
            "DATABASE_URL",
            default="postgresql://postgres:h4yuasd6@127.0.0.1:5432/local-django",
        )
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# S3 Storage Settings

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = config("AWS_S3_ENDPOINT_URL")
AWS_S3_FILE_OVERWRITE = False

STORAGES = {
    # Media files management
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
    # CSS and JS files management
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email Settings

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_USE_SSL = config("EMAIL_SECURE", cast=bool)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Crispy Forms Settings

CRISPY_ALLOWED_TEMPLATE_PACK = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# Custom User Model

AUTH_USER_MODEL = "users.AuthUser"


# External APIs Secret Keys

OPENAI_API_KEY = config("OPENAI_API_KEY", default="just-a-key")
OPENAI_ASSISTANT_ID = config("OPENAI_ASSISTANT_ID", default="just-a-key")


# Social Auth

AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

SOCIAL_AUTH_URL_NAMESPACE = "website:user_auth:social"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "website:static_pages:home"
SOCIAL_AUTH_LOGIN_URL = "/"
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config("GOOGLE_APP_ID")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config("GOOGLE_APP_SECRET")
SOCIAL_AUTH_FACEBOOK_KEY = config("FB_APP_ID")
SOCIAL_AUTH_FACEBOOK_SECRET = config("FB_APP_SECRET")
SOCIAL_AUTH_FACEBOOK_API_VERSION = "19.0"
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email", "public_profile"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    "fields": "email,first_name,last_name",
}

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.social_auth.associate_by_email",
    "users.social_auth_pipelines.create_user",
    # 'users.social_auth_pipelines.get_profile_picture',
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)


# Heroku Logging

logging.config.dictConfig(json.load(open("logging.config.json")))
