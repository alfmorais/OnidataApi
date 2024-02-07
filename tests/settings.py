import os

from src.onidata.settings import *  # noqa

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "tests.sqlite3"),  # noqa F403
    }
}
