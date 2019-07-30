# REST APIs with Flask and Python

## Getting started

**With [Docker Compose](https://docs.docker.com/compose/install/):**

```bash
cp .env.example .env
docker-compose up --build
```

**With [Pipenv](https://github.com/pypa/pipenv):**

```bash
pipenv install && pipenv shell
cp .env.example .env

# Start server
./init.sh
```

Check http://localhost:5000/api/student/John

## Details

### Requirements

- `Flask-Migrate` - for handling all database migrations.
- `Flask-RESTful` - restful API library.
- `Flask-Script` - provides support for writing external scripts.
- `Flask-SQLAlchemy` - adds support for SQLAlchemy ORM.

### Project structure

```
.
├── .env
├── .env_template
├── .gitignore
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── db_data
├── docker-compose.yml
├── init.sh
├── myapp
│   ├── __init__.py
│   ├── app.py
│   ├── endpoints
│   │   ├── __init__.py
│   │   ├── todos
│   │   │   ├── __init__.py
│   │   │   ├── model.py
│   │   │   └── resource.py
│   │   └── users
│   │       ├── model.py
│   │       └── resource.py
│   └── manage.py
├── requirements-dev.txt
└── requirements.txt
```

## API Document

POST http://127.0.0.1:5000/api/users

Content

```json
{
    "name": "John John"
}
```

PUT http://127.0.0.1:5000/api/users/1

```json
{
    "name": "Smith Smith"
}
```

DELETE http://127.0.0.1:5000/api/users/1

GET http://127.0.0.1:5000/api/users

GET http://127.0.0.1:5000/api/users/2

GET http://127.0.0.1:5000/api/users?name=John%20John

GET http://127.0.0.1:5000/api/users?limit=1&offset=1

## References

- [nickjj - build-a-saas-app-with-flask](https://github.com/nickjj/build-a-saas-app-with-flask)
- [Video - REST APIs with Flask and Python](https://youtu.be/rHA5h9Gu7WI)
- [tomasrasymas - flask-restful-api-templa](https://github.com/tomasrasymas/flask-restful-api-template)
- [miguelgrinberg - Migrating from Flask-Script to the New Flask CLI](https://blog.miguelgrinberg.com/post/migrating-from-flask-script-to-the-new-flask-cli)
- [Enabling the Flask Interactive Debugger in Development with gunicorn](https://nickjanetakis.com/blog/enabling-the-flask-interactive-debugger-in-development-with-gunicorn)
