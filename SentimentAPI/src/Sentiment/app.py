from flask import Flask
from flask_cors import CORS
from Sentiment.api.extensions import api
from Sentiment.api.resources import ns
# import torch

def create_app():
    app = Flask(__name__)

    CORS(app)
    api.init_app(app)
    api.add_namespace(ns)
    
    return app