"""Script defining all the procedure needed for database management for the microservice."""
import sqlite3

import click
from flask import current_app, g, Flask
from flask.cli import with_appcontext

def get_db():
    """Procedure to get the database connection for the microservice."""
    # If the db is not defined in the app's global context
    # NOTE: g is a special object that is unique for each request.
    if 'db' not in g:
        # Connect to the database
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    # Return the database connection
    return g.db


def close_db(e=None):
    """Check if a connection was created by checking if g.db was set.
    
    If the connection exists, it is closed.

    Args:
        e (_type_, optional): _description_. Defaults to None.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """Procedure to initialize the the database within the Flask App."""
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app_db_procedures(app: Flask):
    """Procedure to call when initializing the app."""
    # Tells Flask to call that function when cleaning up after returning the response.
    app.teardown_appcontext(close_db)
    
    # Add a new command that can be called with the flask command.
    app.cli.add_command(init_db_command)