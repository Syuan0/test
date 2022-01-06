from flask import Blueprint
from flask_restx import Api

api_blueprint = Blueprint("open_api", __name__)
api = Api(api_blueprint, version="1.0",title="TestSqlalchmy", description="Test config")