from app.main import db
from app.main.model.board import Label


def get_label():
    label_data = Label.query.all()
    label_list = map_label_data(label_data)
    return label_list


def map_label_data(data):
    label_list = []
    for each in data:
        label = {}
        label["id"] = each.id
        label["name"] = each.name
        label_list.append(label)
    return label_list