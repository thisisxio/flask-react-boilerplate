from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    CORS(app)

    from .routes import initialize_routes
    initialize_routes(api)

    #Import models
    from . import models

    return app