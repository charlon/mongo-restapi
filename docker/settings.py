from .base_settings import *

INSTALLED_APPS += [
    "mongo_rest.apps.AppNameConfig",
]

# If you have file data, define the path here
# DATA_ROOT = os.path.join(BASE_DIR, "mongo_rest/data")

GOOGLE_ANALYTICS_KEY = os.getenv("GOOGLE_ANALYTICS_KEY", default=" ")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": True,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "mongo_rest.context_processors.google_analytics",
                "mongo_rest.context_processors.django_debug",
            ],
        },
    }
]


if os.getenv("ENV") == "localdev":
    DEBUG = True

if os.getenv("ENV") == "localdev":
    VITE_MANIFEST_PATH = os.path.join(
        BASE_DIR, "mongo_rest", "static", "manifest.json"
    )
else:
    VITE_MANIFEST_PATH = os.path.join(os.sep, "static", "manifest.json")
