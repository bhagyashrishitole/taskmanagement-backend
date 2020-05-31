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

def validate_get_all_boards(data):
    if not data.get("user_id"):
        return get_response(400, "'user_id' field missing in the request", []), 400