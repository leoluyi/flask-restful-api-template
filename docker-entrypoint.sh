#!/bin/sh

# For flask script
export FLASK_APP="myapp.flasky"
flask db init
flask db migrate
flask db upgrade

# Run app
gunicorn -c python:config.gunicorn "myapp.app:create_app()"
