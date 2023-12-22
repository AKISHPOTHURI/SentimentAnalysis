from flask import Flask

from .utils.extensions import api
from .resourses import ns

def create_app():
    app = Flask(__name__)


    api.init_app(app)
    api.add_namespace(ns)
    
    return app