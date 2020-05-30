from app.main import db
from app.main.model.board import Status


def get_status():
    status_data = Status.query.all()
    status_list = map_status_data(status_data)
    return status_list

def map_status_data(data):
    status_list = []
    for each in data:
        status = {}
        status["id"] = each.id
        status["name"] = each.name
        status_list.append(status)
    return status_list