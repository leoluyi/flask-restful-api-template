FROM python:3.7-slim
MAINTAINER Leo Lu <leo0650@gmail.com>

ENV INSTALL_PATH /my_app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "snakeeyes.app:create_app()"
