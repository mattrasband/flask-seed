from flask import Blueprint
from flask.ext.restful import (
    Api,
    Resource,
)

controller = Blueprint('api', __name__)
api = Api(controller)


@api.resource('/greet')
class GreeterView(Resource):
    def get(self):
        return 'Hello from a GET'

    def post(self):
        return 'Hello from a POST'
