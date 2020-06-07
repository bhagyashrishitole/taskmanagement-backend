from flask_restx import Resource
from ..util.dto import BoardDto
from ..service import board_service
from ..service.auth_helper import Auth
from flask import request

api = BoardDto.api


@api.route('/')
class Board(Resource):
    @api.doc('add board')
    def post(self):
        """create board"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = request.json
            data["user_id"] = resp
            return board_service.add_board(data=data)
        except Exception as e:
            return {'status': 500,
                    'message': "Internal application error."}, 500

@api.route('/<board_id>')
class Board(Resource):
    @api.doc('get single board details')
    def get(self, board_id):
        """get single board details"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = {"user_id": resp}
            return board_service.get_board(board_id=int(board_id), data=data)
        except Exception as e:
            return {'status': 500,
                    'message': "Internal application error."}, 500

    @api.doc('get single board details')
    def delete(self, board_id):
        """get single board details"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = {"user_id": resp}
            return board_service.delete_board(board_id=int(board_id), data=data)
        except Exception as e:
            return {'status': 500,
                    'message': "Internal application error."}, 500


@api.route('/all')
class Board(Resource):
    @api.doc('get all board details')
    def get(self):
        """List all boards"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = {"user_id": resp}
            print("data",data)
            return board_service.get_all_boards(data)
        except Exception as e:
            print(e)
            return {'status': 500,
                    'message': "Internal application error."}, 500


""" Task APIs"""


@api.route('/<board_id>/tasks')
class Board(Resource):
    @api.doc('Add task under board')
    def post(self, board_id):
        """get single board details"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = request.json
            data["user_id"] = resp
            return board_service.add_task_for_board(board_id=int(board_id), data=data)
        except Exception as e:
            print(e)
            return {'status': 500,
                    'message': "Internal application error."}, 500

    @api.doc('Get tasks under board')
    def get(self, board_id):
        """get board task based on filter"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = {"user_id": resp}
            data["query"] = request.args.get('query')
            data["status"] = request.args.get('status')
            data["priority"] = request.args.get('priority')
            data["to"] = request.args.get('to')
            data["from"] = request.args.get('from')
            data["label"] = request.args.get('label')
            return board_service.get_filtered_task(board_id=int(board_id), data=data)
        except Exception as e:
            return {'status': 500,
                    'message': "Internal application error."}, 500

@api.route('/<board_id>/search')
class Board(Resource):
    @api.doc('search for tasks under board')
    def post(self, board_id):
        """search for tasks"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = request.json
            data["user_id"] = resp
            return board_service.search_tasks(board_id=int(board_id), data=data)
        except Exception as e:
            return {'status': 500,
                    'message': "Internal application error."}, 500

@api.route('/<board_id>/tasks/<task_id>')
class Board(Resource):
    @api.doc('Get task under board')
    def get(self, board_id, task_id):
        """get single board details"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = {"user_id": resp}
            return board_service.get_task(board_id=int(board_id), task_id=task_id, data=data)
        except Exception as e:
            return {'status': 500,
                    'message': "Internal application error."}, 500

    @api.doc('Update task under board')
    def put(self, board_id, task_id):
        """update single task details"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = request.json
            data["user_id"] = resp
            return board_service.update_task_for_board(board_id=int(board_id), task_id=task_id, data=data)
        except Exception as e:
            return {'status': 500,
                    'message': "Internal application error."}, 500

    @api.doc('Archive task under board')
    def delete(self, board_id, task_id):
        """archive single task details"""
        try:
            resp = Auth.get_user_id(request.headers)
            if not isinstance(resp, int):
                return resp
            data = {"user_id": resp}
            return board_service.archive_task_for_board(board_id=int(board_id), task_id=task_id, data=data)
        except Exception as e:
            return {'status': 500,
                    'message': "Internal application error."}, 500
