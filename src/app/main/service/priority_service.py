from app.main.service.response import get_response


def get_priority():
    return ["High", "Medium", "Low"]
    # priority_data = Priority.query.all()
    # priority_list = map_priority_data(priority_data)
    # return priority_list


def get_all_priority():
    priority = get_priority()
    return get_response(200, "", priority)


def map_priority_data(data):
    priority_list = []
    for each in data:
        priority = {}
        priority["id"] = each.id
        priority["name"] = each.name
        priority_list.append(priority)
    return priority_list
