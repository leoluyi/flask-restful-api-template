# REST APIs with Flask and Python

## Getting started

1. `pipenv install && pipenv shell`
2. `cp .env.example .env`
3. Run following commands for db migration:

    ```bash
    $ export FLASK_APP="myapp.flasky"
    $ flask db init
    $ flask db migrate
    $ flask db upgrade
    ```

4. Start server by running `./init.sh`
5. Check http://localhost:5000/api/student/John

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

```
{
    "name": "John John"
}
```

PUT http://127.0.0.1:5000/api/users/1

```
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

- [REST APIs with Flask and Python](https://youtu.be/rHA5h9Gu7WI)
- https://github.com/tomasrasymas/flask-restful-api-template
- [Migrating from Flask-Script to the New Flask CLI](https://blog.miguelgrinberg.com/post/migrating-from-flask-script-to-the-new-flask-cli)
