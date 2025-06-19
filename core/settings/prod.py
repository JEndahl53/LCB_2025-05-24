# core/settings/prod.py
from .base import *

DEBUG = False
ADMINS = [
    ("jendahl", "john@endahl.us"),
]
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
