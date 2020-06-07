# from app.main.model.board import Status
from app.main.service.response import get_response


def get_status():
    return ["New", "InProgress", "Completed"]
    # status_data = Status.query.all()
    # status_list = map_status_data(status_data)
    # return status_list


def get_all_status():
    status = get_status()
    return get_response(200, "", status)


def map_status_data(data):
    status_list = []
    for each in data:
        status = {}
        status["id"] = each.id
        status["name"] = each.name
        status_list.append(status)
    return status_list
