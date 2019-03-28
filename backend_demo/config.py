import os
from datetime import timedelta

SECRET_KEY = os.urandom(24)

PERMANENT_SESSION_TIME = timedelta(days=7)