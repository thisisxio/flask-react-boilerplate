# backend/app/resources/property.py
from flask_restful import Resource, reqparse
from app.models import Property
from app import db

class PropertyResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('address', type=str, required=True, help="Address is required")
    parser.add_argument('city', type=str, required=True, help="City is required")
    parser.add_argument('state', type=str, required=True, help="State is required")
    parser.add_argument('price', type=float, required=True, help="Price is required")
    parser.add_argument('bedrooms', type=int, required=True, help="Number of bedrooms is required")
    parser.add_argument('bathrooms', type=int, required=True, help="Number of bathrooms is required")
    parser.add_argument('area', type=int, required=True, help="Area (in sq ft) is required")


    def get(self):
        properties = Property.query.all()
        print(properties)
        return [property.to_dict() for property in properties], 200

    def post(self):
        args = self.parser.parse_args()
        
        #Create New Property instance
        new_property = Property(
            address=args['address'],
            city=args['city'],
            state=args['state'],
            price=args['price'],
            bedrooms=args['bedrooms'],
            bathrooms=args['bathrooms'],
            area=args['area']
        )

        try:
            db.session.add(new_property)
            db.session.commit()
            return new_property.to_dict(), 201  # Return the newly created property
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error adding property: ' + str(e)}, 500
