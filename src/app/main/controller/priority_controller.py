from flask_restx import Resource
from ..util.dto import PriorityDto
from ..service import priority_service
api = PriorityDto.api


@api.route('/all')
class Priority(Resource):
    @api.doc('get list of all priority')
    def get(self):
        """get list of all priority"""
        return priority_service.get_all_priority()