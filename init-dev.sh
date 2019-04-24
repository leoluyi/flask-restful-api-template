#!/usr/bin/env bash

export FLASK_ENV="development"
./db-migration.sh
# pipenv run gunicorn -b 0.0.0.0:5000 --access-logfile - "myapp.app:create_app()"
pipenv run gunicorn -c python:config.gunicorn "myapp.app:create_app()"
