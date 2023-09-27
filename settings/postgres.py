"""Postgres settings."""

import os

from settings.base import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME", "django_dynaform"),
        "USER": os.getenv("DATABASE_USER", "postgres"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "postgres"),
        "HOST": os.getenv("DATABASE_HOST", "localhost"),
        "PORT": 5432,
    }
}
