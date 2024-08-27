from flask import Flask
from json import JSONEncoder
from decimal import Decimal
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(CustomJSONEncoder, self).default(obj)

def create_app():
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
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