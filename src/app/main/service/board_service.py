import datetime

from app.main.service.response import get_response
from app.main.service.label_service import get_label
from app.main.service.priority_service import get_priority
from app.main.service.status_service import get_status
from app.main import db
from app.main.model.board import Board, Task
from ..service import validator
from ..service.auth_helper import Auth

def add_board(data):
    not_valid = validator.validate_add_board(data)
    if not_valid:
        return not_valid
    new_board = Board(
        name=data['name'],
        user_id=data['user_id']
    )
    save_changes(new_board)
    return get_response(200, "{} board created".format(data['name']), []), 200


def get_all_boards(data):
    not_valid = validator.validate_get_all_boards(data)
    if not_valid:
        return not_valid
    board_data = Board.query.filter_by(user_id=data['user_id']).all()
    board_details_list = map_board_data(board_data)
    return get_response(200, "", board_details_list), 200


def get_board(board_id, data):
    not_valid = validator.validate_get_board(data)
    if not_valid:
        return not_valid
    task_data = Task.query.filter_by(user_id=data['user_id'], board_id=board_id, is_archived=False).all()
    task_details_list = map_task_data(task_data)
    data = {
        "tasks": task_details_list,
        "label": get_label(),
        "priority": get_priority(),
        "task_status": get_status()
    }
    return get_response(200, "", data), 200


def delete_board(board_id, data):
    not_valid = validator.validate_delete_board(data)
    if not_valid:
        return not_valid
    Task.query.filter_by(user_id=data['user_id'], board_id=board_id).delete()
    Board.query.filter_by(user_id=data['user_id'], id=board_id).delete()
    db.session.commit()
    return get_response(200, "Deleted Board", []), 200


def add_task_for_board(board_id, data):
    not_valid = validator.validate_add_task(data)
    if not_valid:
        return not_valid
    labels = data.get("label") if data.get("label") else []
    new_task = Task(
        title=data['title'],
        board_id=board_id,
        user_id=data['user_id'],
        status=data['status'],
        desc=data.get('desc'),
        label_personal="Personal" if "Personal" in labels else None,
        label_work="Work" if "Work" in labels else None,
        label_shopping="Shopping" if "Shopping" in labels else None,
        label_others="Others" if "Others" in labels else None,
        priority=data.get('priority'),
        creation_date=datetime.datetime.utcnow(),
        update_date=datetime.datetime.utcnow(),
		due_date = datetime.datetime.strptime(data.get("due_date"), "%Y/%m/%d") if data.get('due_date') else None
    )
    save_changes(new_task)
    return get_response(200, "{} task created".format(data['title']), []), 200

def get_filtered_task(board_id, data):
    query = Task.query.filter_by(board_id=board_id, user_id=data["user_id"], is_archived=False)
    if data.get("status"):
        query = query.filter_by(status=data["status"])

    if data.get("priority"):
        query = query.filter_by(priority=data["priority"])
    if data.get("query"):
        query =  query.filter((Task.title.like("%{}%".format(data["query"])))|
                              (Task.desc.like("%{}%".format(data["query"]))))
    if data.get("to") and data.get("from"):
        to_date = datetime.datetime.strptime(data.get("to"), "%Y/%m/%d")
        from_date = datetime.datetime.strptime(data.get("from"), "%Y/%m/%d")
        query = query.filter(Task.due_date.between(from_date, to_date))

    if data.get("label"):
        label = data["label"]
        if label == "Personal":
            query = query.filter_by(label_personal=label)
        if label == "Work":
            query = query.filter_by(label_work=label)
        if label == "Shopping":
            query = query.filter_by(label_shopping=label)
        if label == "Others":
            query = query.filter_by(label_others=label)
    print(query)
    task_data = query.all()
    task_details_list = map_task_data(task_data)
    return get_response(200, "", task_details_list), 200

def get_task(board_id, task_id, data):
    task_data = Task.query.filter_by(id=task_id, board_id=board_id, user_id=data["user_id"]).all()
    task_details_list = map_task_data(task_data)
    data = []
    if task_details_list:
        data = task_details_list[0]

    return get_response(200, "", data), 200


def update_task_for_board(board_id, task_id, data):
    not_valid = validator.validate_update_task_for_board(data)
    if not_valid:
        return not_valid
    task_data = Task.query.filter_by(id=task_id, board_id=board_id, user_id=data["user_id"]).first()
    if task_data:
        if data.get("is_archived") is not None:
            task_data.is_archived = data.get("is_archived")
        if data.get("due_date"):
            task_data.due_date = datetime.datetime.strptime(data.get("due_date"), "%Y/%m/%d")
        if data.get("status"):
            task_data.status = data.get("status")
        if data.get("priority"):
            task_data.priority = data.get("priority")
        if data.get("title"):
            task_data.title = data['title']
        if data.get("desc"):
            task_data.desc = data['desc']
        if data.get("label"):
            labels = data.get("label")
            task_data.label_personal = "Personal" if "Personal" in labels else None
            task_data.label_work = "Work" if "Work" in labels else None
            task_data.label_shopping = "Shopping" if "Shopping" in labels else None
            task_data.label_others = "Others" if "Others" in labels else None

        task_data.update_date = datetime.datetime.utcnow()
        db.session.commit()
        return get_response(200, "{} task updated.".format(task_data.title), []), 200
    else:
        return get_response(404, "{} task didn't found.".format(task_id), []), 404


def archive_task_for_board(board_id, task_id, data):
    task_data = Task.query.filter_by(id=task_id, board_id=board_id, user_id=data["user_id"]).first()
    if task_data:
        task_data.is_archived = True
        db.session.commit()
        return get_response(200, "{} task archived.".format(task_data.title), []), 200
    else:
        return get_response(404, "{} task didn't found.".format(task_id), []), 404


def search_tasks(board_id, data):
    query = Task.query.filter_by(board_id=board_id, user_id=data["user_id"], is_archived=False)
    if data.get("status"):
        query = query.filter_by(status=data["status"])

    if data.get("priority"):
        query = query.filter_by(priority=data["priority"])
    if data.get("query"):
        query = query.filter((Task.title.like("%{}%".format(data["query"]))) |
                             (Task.desc.like("%{}%".format(data["query"]))))
    if data.get("to") and data.get("from"):
        to_date = datetime.datetime.strptime(data.get("to"), "%Y/%m/%d")
        from_date = datetime.datetime.strptime(data.get("from"), "%Y/%m/%d")
        query = query.filter(Task.due_date.between(from_date, to_date))

    if data.get("label"):
        label = data["label"]
        if label == "Personal":
            query = query.filter_by(label_personal=label)
        if label == "Work":
            query = query.filter_by(label_work=label)
        if label == "Shopping":
            query = query.filter_by(label_shopping=label)
        if label == "Others":
            query = query.filter_by(label_others=label)
    print(query)
    task_data = query.all()
    task_details_list = map_task_data(task_data)
    return get_response(200, "", task_details_list), 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def map_board_data(board_data):
    board_details_list = []
    for each in board_data:
        board = {}
        board["id"] = each.id
        board["name"] = each.name
        board_details_list.append(board)
    return board_details_list


def map_task_data(task_data):
    task_details_list = []
    for each in task_data:
        task = {}
        task["id"] = each.id
        task["title"] = each.title
        task["labels"] = []
        if each.label_personal:
            task["labels"].append(each.label_personal)
        if each.label_work:
            task["labels"].append(each.label_work)
        if each.label_shopping:
            task["labels"].append(each.label_shopping)
        if each.label_others:
            task["labels"].append(each.label_others)

        task["desc"] = each.desc
        task["board_id"] = each.board_id
        task["status"] = each.status
        task["priority"] = each.priority
        task["creation_date"] = each.creation_date.strftime("%Y/%m/%d")
        if each.due_date:
            task["due_date"] = each.due_date.strftime("%Y/%m/%d")
        else:
            task["due_date"] = each.due_date
        task["update_date"] = each.update_date.strftime("%Y/%m/%d")
        task["is_archived"] = each.is_archived
        task_details_list.append(task)
    return task_details_list
