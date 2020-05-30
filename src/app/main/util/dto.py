from flask_restx import Namespace, fields


class PingDto:
    api = Namespace("ping", description="Default ping resource")

class BoardDto:
    api = Namespace('board', description='board related operations')

