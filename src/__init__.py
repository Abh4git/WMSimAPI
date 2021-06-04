from flask import Flask

#We will be using the application factory pattern for creating our
#Flask object.
from flask_cors import CORS, cross_origin
from src.config import config_by_name
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    return app