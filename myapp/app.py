from .endpoints.users.resource import UsersResource
from .endpoints.todos.resource import TodosResource
from .extensions import (
    api,
    db,
)
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_restful import Resource
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
import os
from pathlib import Path
load_dotenv()


class Student(Resource):
    """docstring for Student"""

    def get(self, name):
        return jsonify({'student': name})


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    if settings_override:
        app.config.update(settings_override)

    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code

    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)

    SQLALCHEMY_DATABASE_URI = Path(os.getenv('SQLALCHEMY_DATABASE_URI')).expanduser().resolve().as_posix()
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLALCHEMY_DATABASE_URI}'
    print(SQLALCHEMY_DATABASE_URI)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['BUNDLE_ERRORS'] = os.getenv('BUNDLE_ERRORS')
    app.config['DEBUG'] = True
    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """

    # DB
    db.init_app(app)

    # API
    api.prefix = '/api'
    api.add_resource(Student, '/student/<string:name>')
    api.add_resource(UsersResource, '/users', '/users/<int:user_id>')
    api.add_resource(TodosResource, '/todos', '/todos/<int:todo_id>')
    api.init_app(app)

    return None
