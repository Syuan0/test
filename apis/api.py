from flask import Blueprint
from flask_restplus import Api

api_blueprint = Blueprint("open_api", __name__)
api = Api(api_blueprint, version="1.0",title="OpenApi", description="The Open Api Service")