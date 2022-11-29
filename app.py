"""Main script to run the microservice."""

from constants import HOST, PORT, DEBUG
from flaskr import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(HOST, PORT, DEBUG)