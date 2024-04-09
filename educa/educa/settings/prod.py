import os
from .base import *  # noqa:F403

DEBUG = False

# fmt:off
ADMIN = [
    ('Akhat A', 'email@email.com'),
]

ALLOWED_HOSTS = ['.educaproject.com', 'www.educaproject.com', 'educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}


REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL  # noqa:F405
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]  # noqa:F405

# security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
