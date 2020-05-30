from flask_restx import Resource
from ..util.dto import LabelDto
from ..service import label_service
api = LabelDto.api


@api.route('/all')
class Label(Resource):
    @api.doc('get list of all labels')
    def get(self):
        """get list of all labels"""
        return label_service.get_all_label()