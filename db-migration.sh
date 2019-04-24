#!/bin/sh

export FLASK_APP="myapp.flasky"
flask db init
flask db migrate
flask db upgrade
