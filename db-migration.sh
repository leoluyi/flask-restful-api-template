#!/usr/bin/env bash

export FLASK_APP="myapp.flasky"
pipenv run flask db init
pipenv run flask db migrate
pipenv run flask db upgrade
