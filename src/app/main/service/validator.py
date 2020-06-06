from ..service.response import get_response
def validate_add_board(data):

    if not data.get("name"):
        return get_response(400, "'name' field missing in the request", []), 400
    if not data.get("user_id"):
        return get_response(400, "'user_id' field missing in the request", []), 400

def validate_delete_board(data):
    if not data.get("user_id"):
        return get_response(400, "'user_id' field missing in the request", []), 400

def validate_get_board(data):
    if not data.get("user_id"):
        return get_response(400, "'user_id' field missing in the request", []), 400

def validate_add_task(data):
    if not data.get("title"):
        return get_response(400, "'title' field missing in the request", []), 400
    if not data.get("status"):
        return get_response(400, "'status' field missing in the request", []), 400

def validate_get_all_boards(data):
    if not data.get("user_id"):
        return get_response(400, "'user_id' field missing in the request", []), 400

def validate_update_task_for_board(data):
    if not data.get("user_id"):
        return get_response(400, "'user_id' field missing in the request", []), 400

def validate_archive_task_for_board(data):
    if not data.get("user_id"):
        return get_response(400, "'user_id' field missing in the request", []), 400
