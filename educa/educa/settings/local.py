from .base import *  # noqa:F403

# fmt: off

DEBUG = True

INSTALLED_APPS += [  # noqa: F405
    "debug_toolbar"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'  # noqa: F405
    }
}
