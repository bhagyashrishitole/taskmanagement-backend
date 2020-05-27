from flask_restx import Resource
from ..util.dto import PingDto

api = PingDto.api


@api.route('/')
class Ping(Resource):
    @api.doc('ping')
    def get(self):
        """Ping-Pong"""
        return "pong"
