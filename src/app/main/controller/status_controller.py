from flask_restx import Resource
from ..util.dto import StatusDto
from ..service import status_service
api = StatusDto.api


@api.route('/all')
class Status(Resource):
    @api.doc('get list of all status')
    def get(self):
        """get list of all status"""
        return status_service.get_all_status()