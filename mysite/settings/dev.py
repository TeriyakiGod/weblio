from decouple import config

from .base import *  # noqa: F403, F401
from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True
INSTALLED_APPS += [
    'debug_toolbar',
    'django_browser_reload',
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]
ALLOWED_HOSTS = ["*"]
EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
INTERNAL_IPS = [
    "127.0.0.1",
]

try:
    from .local import *  # noqa: F403, F401
except ImportError:
    pass
