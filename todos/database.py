import sqlite3
import click
from flask import current_app, g

def init_app(app): # uses click to add database initialization command to Flask's CLI
    app.teardown_appcontext(close_db) # close the database connection when the app is done processing
    app.cli.add_command(init_db_command)

@click.command("init-db")
def init_db_command(): # get a database connection
    db = get_db()

    with current_app.open_resource("schema.sql") as f: # read & execute SQL commands from schema.sql
        db.executescript(f.read().decode("utf-8"))

    click.echo("You successfully initialized the database!") # print message indicating database successfully initialized

def get_db(): # return database connection (new or established)
    if "db" not in g: # use sqlite module to create database connection for database named in environment variables
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row # grant access to the columns by name

    return g.db
    
def close_db(e=None):
    db = g.pop("db", None)
     
    if db is not None:
        db.close()