# backend/app/routes.py
from .resources.property import PropertyResource
# from .resources.user import UserResource

def initialize_routes(api):
    api.add_resource(PropertyResource, '/api/properties')
    # api.add_resource(UserResource, '/api/users')
    
