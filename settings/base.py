"""Base settings."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "my-secret-key"

INSTALLED_APPS = [
    "tests",
    "dynaform",
]

USE_TZ = True

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
