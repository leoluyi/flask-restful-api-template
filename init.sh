#!/usr/bin/env bash

# export FLASK_APP="myapp.app:create_app()"
# flask run
gunicorn -b 0.0.0.0:5000 --access-logfile - "myapp.app:create_app()"
