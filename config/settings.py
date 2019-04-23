from distutils.util import strtobool
from pathlib import Path
import os

SECRET_KEY = os.getenv('SECRET_KEY', None)
SERVER_NAME = os.getenv('SERVER_NAME',
                        f'localhost:{os.getenv("DOCKER_WEB_PORT", "5000")}')
BUNDLE_ERRORS = bool(strtobool(os.getenv('BUNDLE_ERRORS')))

# DB and SQLAlchemy
_ = Path(os.getenv('SQLALCHEMY_DATABASE_URI')).expanduser().resolve().as_posix()
SQLALCHEMY_DATABASE_URI = f'sqlite:///{_}'
print(f'(SQLite URI) {SQLALCHEMY_DATABASE_URI}')

SQLALCHEMY_TRACK_MODIFICATIONS = bool(strtobool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')))
