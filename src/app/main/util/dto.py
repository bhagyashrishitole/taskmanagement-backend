from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

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

