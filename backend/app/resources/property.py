# backend/app/resources/property.py
from flask_restful import Resource
from app.models import Property
from app import db

class PropertyResource(Resource):
    def get(self):
        properties = Property.query.all()
        print(properties)
        return [{'id': p.id, 'address': p.address, 'price': str(p.price)} for p in properties]
