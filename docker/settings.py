from .base_settings import *
from mongoengine import connect

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'webpack_loader',
    'rest_framework'
    'rest_framework_mongoengine',
    'mongo_rest'
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'mongo_rest/bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'mongo_rest', 'static', 'webpack-stats.json'),
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DATA_ROOT = os.path.join(BASE_DIR, "mongo_rest/data")

GOOGLE_ANALYTICS_KEY = os.getenv("GOOGLE_ANALYTICS_KEY", default=" ")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug':  True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mongo_rest.context_processors.google_analytics',
                'mongo_rest.context_processors.django_debug',
            ],
        }
    }
]

if os.getenv("ENV") == "localdev":
    DEBUG = True

mongoengine.connect(
    db="my-database-name",
    username='YourUsername',
    password='YourPasswordHere',
    host='localhost'
)