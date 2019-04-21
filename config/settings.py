from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv()


_ = Path(os.getenv('SQLALCHEMY_DATABASE_URI')).expanduser().resolve().as_posix()
SQLALCHEMY_DATABASE_URI = f'sqlite:///{_}'
print(f'(SQLite URI) {SQLALCHEMY_DATABASE_URI}')

SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
BUNDLE_ERRORS = os.getenv('BUNDLE_ERRORS')
SECRET_KEY = os.getenv('SECRET_KEY', None)
