import datetime

from app.main.service.response import get_response
from app.main.service.label_service import get_label
from app.main.service.priority_service import get_priority
from app.main.service.status_service import get_status
from app.main import db
from app.main.model.board import Board, Task, Label, Priority
from ..service import validator


def add_board(data):
    not_valid = validator.validate_add_board(data)
    if not_valid:
        return not_valid
    new_board = Board(
        name = data['name'],
        user_id = data['user_id']
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
    task_data = Task.query.filter_by(user_id=data['user_id'], board_id=board_id).all()
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
    d ={}
    for each in data.get("label"):
        d[each] = each

    new_task = Task(
        title = data['title'],
        board_id = board_id,
        user_id = data['user_id'],
        status = data['status'],
        desc = data.get('desc'),
        label_personal = "Personal" if "Personal" in data["label"] else None,
        label_work="Work" if "Work" in data["label"] else None,
        label_shopping="Shopping" if "Shopping" in data["label"] else None,
        label_others="Others" if "Others" in data["label"] else None,
        priority = data.get('priority'),
        creation_date = datetime.datetime.utcnow(),
        update_date = datetime.datetime.utcnow()
    )
    save_changes(new_task)
    return get_response(200, "{} task created".format(data['title']), []), 200

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
        if data.get("due_date"):
            task_data.due_date = datetime.datetime.strptime(data.get("due_date"), "%m/%d/%Y, %H:%M:%S")
        if data.get("status"):
            task_data.status = data.get("status")
        if data.get("priority"):
            task_data.priority = data.get("priority")
        if data.get("label"):
            labels = []
            if task_data.label_personal:
                labels.append(task_data.label_personal)
            if task_data.label_work:
                labels.append(task_data.label_work)
            if task_data.label_shopping:
                labels.append(task_data.label_shopping)
            if task_data.label_others:
                labels.append(task_data.label_others)

            for i in range(len(data.get("label"))):
                if data["label"][i] not in labels:
                    labels.append(data.get("label")[i])

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
    not_valid = validator.validate_archive_task_for_board(data)
    if not_valid:
        return not_valid
    task_data = Task.query.filter_by(id=task_id, board_id=board_id, user_id=data["user_id"]).first()
    if task_data:
        task_data.is_archived = True
        db.session.commit()
        return get_response(200, "{} task archived.".format(task_data.title), []), 200
    else:
        return get_response(404, "{} task didn't found.".format(task_id), []), 404


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
        task["creation_date"] = each.creation_date.strftime("%m/%d/%Y, %H:%M:%S")
        if each.due_date:
            task["due_date"] = each.due_date.strftime("%m/%d/%Y, %H:%M:%S")
        # task["due_date"] = each.due_date
        task["update_date"] = each.update_date.strftime("%m/%d/%Y, %H:%M:%S")
        task["is_archived"] = each.is_archived
        task_details_list.append(task)
    return task_details_list



