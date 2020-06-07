from app.main.service.response import get_response


def get_label():
    return ["Personal", "Work", "Shopping", "Others"]
    # label_data = Label.query.all()
    # label_list = map_label_data(label_data)
    # return label_list


def get_all_label():
    labels = get_label()
    return get_response(200, "", labels)


def map_label_data(data):
    label_list = []
    for each in data:
        label = {}
        label["id"] = each.id
        label["name"] = each.name
        label_list.append(label)
    return label_list
