from app.main import db
from app.main.model.board import Priority


def get_priority():
    priority_data = Priority.query.all()
    priority_list = map_priority_data(priority_data)
    return priority_list

def map_priority_data(data):
    priority_list = []
    for each in data:
        priority = {}
        priority["id"] = each.id
        priority["name"] = each.name
        priority_list.append(priority)
    return priority_list