#!/bin/sh

export FLASK_APP="myapp.flasky"
flask db init
flask db migrate
flask db upgrade

gunicorn -c python:config.gunicorn "myapp.app:create_app()"
