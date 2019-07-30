from distutils.util import strtobool
from pathlib import Path
import os

# Flask App.
SECRET_KEY = os.getenv('SECRET_KEY', None)
# SERVER_NAME = os.getenv('SERVER_NAME',
#                         f'localhost:{os.getenv("DOCKER_WEB_PORT", "5000")}')

# DB and SQLAlchemy.
_ = Path(os.getenv('SQLALCHEMY_DATABASE_URI')).expanduser().resolve().as_posix()
SQLALCHEMY_DATABASE_URI = f'sqlite:///{_}'
print(f'(SQLite URI) {SQLALCHEMY_DATABASE_URI}')

SQLALCHEMY_TRACK_MODIFICATIONS = bool(strtobool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')))

# Flask-RESTful.
BUNDLE_ERRORS = bool(strtobool(os.getenv('BUNDLE_ERRORS')))

# Flask-Mail.
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = os.getenv('MAIL_PORT', 587)
MAIL_USE_TLS = bool(strtobool(os.getenv('MAIL_USE_TLS', 'true')))
MAIL_USE_SSL = bool(strtobool(os.getenv('MAIL_USE_SSL', 'false')))
MAIL_USERNAME = os.getenv('MAIL_USERNAME', None)
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', None)
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'smtp.gmail.com')

# Celery.
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
