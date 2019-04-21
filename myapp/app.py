from .endpoints.users.resource import UsersResource
from .endpoints.todos.resource import TodosResource
from .extensions import (
    api,
    db,
)
from flask import Flask, jsonify
from flask_restful import Resource
from werkzeug.exceptions import default_exceptions, HTTPException
from werkzeug.debug import DebuggedApplication


class Student(Resource):
    """docstring for Student"""

    def get(self, name):
        return jsonify({'student': name, 'test': 1 / 0})


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')

    if settings_override:
        app.config.update(settings_override)

    extensions(app)

    if app.debug:
        print('!!! Debug mode !!!')
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    else:
        @app.errorhandler(Exception)
        def handle_error(e):
            code = 500
            if isinstance(e, HTTPException):
                code = e.code
            return jsonify(error=str(e)), code

        for exc in default_exceptions:
            app.register_error_handler(exc, handle_error)

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
