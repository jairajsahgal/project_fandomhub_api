"""Settings for config project (Base)."""

import os
from pathlib import Path
from datetime import timedelta
import environ


BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env("config/.env")

BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.utils",
    "apps.categories",
    "apps.contents",
    "apps.persons",
    "apps.profiles",
    "apps.searches",
    "apps.users",
    "apps.watchlists",
]

THIRD_APPS = [
    "corsheaders",
    "rest_framework",
    "djoser",
    "social_django",
    "modeltranslation",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "debug_toolbar",
]

INSTALLED_APPS = BASE_APPS + PROJECT_APPS + THIRD_APPS

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"

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

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", "English"),
    ("ja", "Japanese"),
    ("es", "Spanish"),
    ("it", "Italian"),
    ("pt", "Portuguese"),
    ("fr", "French"),
    ("de", "German"),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = "en"

MODELTRANSLATION_LANGUAGES = ("en", "ja", "es",)

MODELTRANSLATION_TRANSLATION_FILES = (
    "apps.contents.translation",
)

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle"
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_CONTENT_LANGUAGE": "en",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    # "DEFAULT_THROTTLE_RATES": {
    #     "anon": "100/day",
    #     "user": "1000/day"
    # },
    "NUM_PROXIES": None,
    "PAGE_SIZE": 2,
    "SEARCH_PARAM": "q",
    "ORDERING_PARAM": "ordering",
    # "DEFAULT_VERSION": "v2",
    # "ALLOWED_VERSIONS": ["v1", "v2"],
    # "VERSION_PARAM": "version",
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT", ),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10080),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESFH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.AccessToken",
    )
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
        "http://localhost:8000/google", "http://localhost:8000/facebook"
    ],
    "SERIALIZERS": {
        "user_create": "apps.users.serializers.UserSerializer",
        "user": "apps.users.serializers.UserCreateSerializer",
        "current_user": "apps.users.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}

AUTH_USER_MODEL = "users.User"

SPECTACULAR_SETTINGS = {
    "TITLE": "Project: Beehive",
    "VERSION": "v1",
    "DESCRIPTION": "The Beehive API provides access to data about beehives, bees, and more",
    "LICENSE": {
        "name": "Apache Licence 2.0",
        "url": "https://github.com/tyronejosee/project_beehive_api/blob/main/LICENSE"
    },
    "CONTACT": {"name": "Developer", "url": "https://github.com/tyronejosee"},
    "SCHEMA_PATH_PREFIX": r"^/api/v\d+",
    "SCHEMA_PATH_PREFIX_TRIM": True,
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
