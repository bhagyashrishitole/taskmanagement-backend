import datetime

from app.main import db
from app.main.model.board import Task
from app.main.service.response import get_response


def add_task_for_board(board_id, data):
    new_task = Task(
        title = data['title'],
        board_id = board_id,
        user_id = data['user_id'],
        status = data['status'],
        desc  = data.get('desc'),
        priority = data.get('priority'),
        creation_date = datetime.datetime.utcnow(),
        update_date = datetime.datetime.utcnow()
    )
    save_changes(new_task)
    return get_response(200, "{} task created".format(data['title']), []), 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def map_task_data(task_data):
    task_details_list = []
    for each in task_data:
        task = {}
        task["id"] = each.id
        task["title"] = each.title
        task["desc"] = each.desc
        task["board_id"] = each.board_id
        task["status"] = each.status
        task["priority"] = each.priority
        task["creation_date"] = each.creation_date.strftime("%m/%d/%Y, %H:%M:%S")
        if each.due_date:
            task["due_date"] = each.due_date.strftime("%m/%d/%Y, %H:%M:%S")
        task["due_date"] = each.due_date
        task["update_date"] = each.update_date.strftime("%m/%d/%Y, %H:%M:%S")
        task["is_archived"] = each.is_archived
        task_details_list.append(task)
    return task_details_list