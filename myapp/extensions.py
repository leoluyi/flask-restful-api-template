from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


db = SQLAlchemy()  # done here so that db is importable
api = Api()
