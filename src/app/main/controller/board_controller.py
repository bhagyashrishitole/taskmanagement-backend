from flask_restx import Resource
from ..util.dto import BoardDto
from ..service import board_service
from flask import request

api = BoardDto.api


@api.route('/')
class Board(Resource):
    @api.doc('add board')
    def post(self):
        """create board"""
        data = request.json
        data["user_id"] = 101
        return board_service.add_board(data=data)


@api.route('/<board_id>')
class Board(Resource):
    @api.doc('get single board details')
    def get(self, board_id):
        """get single board details"""
        data = request.json
        data["user_id"] = 101
        return board_service.get_board(board_id=int(board_id), data=data)

    @api.doc('get single board details')
    def delete(self, board_id):
        """get single board details"""
        data = request.json
        data["user_id"] = 101
        return board_service.delete_board(board_id=int(board_id), data=data)


@api.route('/all')
class Board(Resource):
    @api.doc('get all board details')
    def get(self):
        """List all boards"""
        data = request.json
        data["user_id"] = 101
        return board_service.get_all_boards(data)


""" Task APIs"""


@api.route('/<board_id>/tasks')
class Board(Resource):
    @api.doc('Add task under board')
    def post(self, board_id):
        """get single board details"""
        data = request.json
        data["user_id"] = 101
        return board_service.add_task_for_board(board_id=int(board_id), data=data)


@api.route('/<board_id>/tasks/<task_id>')
class Board(Resource):
    @api.doc('Add task under board')
    def get(self, board_id, task_id):
        """get single board details"""
        data = request.json
        data["user_id"] = 101
        return board_service.get_task(board_id=int(board_id), task_id=task_id, data=data)

    @api.doc('Update task under board')
    def put(self, board_id, task_id):
        """update single task details"""
        data = request.json
        data["user_id"] = 101
        return board_service.update_task_for_board(board_id=int(board_id), task_id=task_id, data=data)

    @api.doc('Archive task under board')
    def delete(self, board_id, task_id):
        """archive single task details"""
        data = request.json
        data["user_id"] = 101
        return board_service.archive_task_for_board(board_id=int(board_id), task_id=task_id, data=data)
