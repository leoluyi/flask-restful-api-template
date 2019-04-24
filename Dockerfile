FROM python:3.7-slim
LABEL maintainer="Leo Lu <leo0650@gmail.com>"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ARG FLASK_ENV="production"
ENV FLASK_ENV="${FLASK_ENV}" \
    PYTHONUNBUFFERED="true"

# Copy App files
COPY . .
RUN chmod +x ./docker-entrypoint.sh

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the app when the container launches
CMD ["./docker-entrypoint.sh"]
