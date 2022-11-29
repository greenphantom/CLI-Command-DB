"""Script defining constants used throughout the app."""

from utils.app_env import ENV as env

# FLASK
HOST = env.get_value('FLASK_HOST', '0.0.0.0')
PORT = int(env.get_value('FLASK_PORT', '5000'))
DEBUG = env.get_bool_value('FLASK_DEBUG', False)