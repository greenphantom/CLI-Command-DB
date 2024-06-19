"""Initialization script for the flask microservice."""
import os

from flask import Flask


def create_app(test_config=None) -> Flask:
    """Procedure to create the flask application.

    Args:
        test_config : Optional config for testing the application. Defaults to None.

    Returns:
        Flask: The configured application
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Welcome to my command app. Please use the /commands route to see all available commands.'

    from . import db
    db.init_app_db_procedures(app)

    from routes.command_route import cmd_route
    app.register_blueprint(cmd_route)

    return app