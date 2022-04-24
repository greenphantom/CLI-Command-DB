"""Main script to run the microservice."""

from flask import Flask
from utils.app_env import AppEnv

def create_app():
    """App factory for starting the Flask microservice app."""
    app = Flask(__name__)
    return app

if __name__ == '__main__':
    env = AppEnv()
    app = create_app()
    app.run(host = env.get_value('FLASK_HOST', '0.0.0.0'), port = int(env.get_value('FLASK_PORT', '5000')), debug=env.get_bool_value('FLASK_DEBUG', True))