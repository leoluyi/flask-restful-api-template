# REST APIs with Flask and Python

## Get started

1. `pipenv install && pipenv shell`
2. Run following commands for db migration:

    ```bash
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
    ```

3. Start server by running `./init.sh`
4. Check http://0.0.0.0:5000/api/student/John

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

## References

- https://youtu.be/rHA5h9Gu7WI
- https://github.com/tomasrasymas/flask-restful-api-template

