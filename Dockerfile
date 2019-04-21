FROM python:3.7-slim
LABEL maintainer="Leo Lu <leo0650@gmail.com>"

WORKDIR /flask

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ARG FLASK_ENV="production"
ENV FLASK_ENV="${FLASK_ENV}" \
    PYTHONUNBUFFERED="true"

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-c", "python:config.gunicorn", "myapp.app:create_app()"]
