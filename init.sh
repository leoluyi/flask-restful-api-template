#!/usr/bin/env bash

# export FLASK_APP="myapp.app:create_app()"
# flask run

pipenv run gunicorn -b localhost:5000 --access-logfile - "myapp.app:create_app()"
