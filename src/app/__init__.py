from flask_restx import Api
from flask import Blueprint

from .main.controller.ping_controller import api as ping_ns
from .main.controller.board_controller import api as board_ns
from .main.controller.status_controller import api as status_ns
from .main.controller.priority_controller import api as priority_ns
from .main.controller.label_controller import api as label_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(ping_ns)
api.add_namespace(board_ns)
api.add_namespace(status_ns)
api.add_namespace(priority_ns)
api.add_namespace(label_ns)