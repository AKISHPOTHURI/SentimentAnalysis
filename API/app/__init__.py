from flask import Flask
from flask_cors import CORS
from .extensions import api
from .resourses import ns

def create_app():
    app = Flask(__name__)

    CORS(app)
    api.init_app(app)
    api.add_namespace(ns)
    
    return app