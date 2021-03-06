"""Flask commands

The flask command is implemented using Click.

References

- [Flask CLI - Custom Commands](https://flask.palletsprojects.com/en/1.1.x/cli/#custom-commands)
- [Migrating from Flask-Script to the New Flask CLI](https://blog.miguelgrinberg.com/post/migrating-from-flask-script-to-the-new-flask-cli)
- https://github.com/miguelgrinberg/flasky/blob/master/flasky.py
"""

from .app import create_app, db
# from app.models import User, Follow, Role, Permission, Post, Comment
from flask_migrate import Migrate
import click
import os

app = create_app(os.getenv('FLASK_CONFIG'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)


@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, help='aaa')
def test(coverage=False):
    "Test coverage"
    # ...
    pass


@app.cli.command()
@click.option('--length', default=25, help='Profile stack length')
@click.option('--profile-dir', default=None, help='Profile directory')
def profile(length, profile_dir):
    """Start the application under the code profiler."""
    # ...
    pass


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # ...
    pass
