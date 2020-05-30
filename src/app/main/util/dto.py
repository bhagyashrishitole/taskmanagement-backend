from flask_restx import Namespace, fields


class PingDto:
    api = Namespace("ping", description="Default ping resource")

class BoardDto:
    api = Namespace('board', description='board related operations')

class StatusDto:
    api = Namespace('status', description='Status related operations')

class PriorityDto:
    api = Namespace('priority', description='Status related operations')

class LabelDto:
    api = Namespace('label', description='Status related operations')

