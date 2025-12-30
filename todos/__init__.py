import os
from dotenv import load_dotenv
from flask import Flask

from todos import lists, items, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)

    app.register_blueprint(lists.bp)
    app.register_blueprint(items.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app