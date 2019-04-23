from .endpoints.users.resource import UsersResource
from .endpoints.todos.resource import TodosResource
from .endpoints.students.resource import StudentsResource
from .extensions import (
    api,
    db,
)
from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException
from werkzeug.debug import DebuggedApplication


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
        jsonify_error_handler(app)

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
    api.add_resource(StudentsResource, '/student/<string:name>')
    api.add_resource(UsersResource, '/users', '/users/<int:user_id>')
    api.add_resource(TodosResource, '/todos', '/todos/<int:todo_id>')
    api.init_app(app)

    return None


def jsonify_error_handler(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code

    for exc in default_exceptions:
        app.register_error_handler(exc, handle_error)
