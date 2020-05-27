from flask_restx import Namespace, fields


class PingDto:
    api = Namespace("ping", description="Default ping resource")
