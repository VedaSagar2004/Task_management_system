from flask import request, jsonify
from functools import wraps
from datetime import datetime
from app.database.datastore import db
from app.common.constants import ErrorMessages, StatusCodes, JWTSecret
import jwt

def validate_task_data(task_data, required_title=True):
    if not task_data:
        return False, ErrorMessages.INVALID_JSON
    if required_title and 'title' not in task_data:
        return False, ErrorMessages.MISSING_TITLE
    if 'due_date' in task_data:
        try:
            datetime.strptime(task_data['due_date'], "%d-%m-%Y")
        except ValueError:
            return False, ErrorMessages.INVALID_DATE_FORMAT
    return True, None


def find_task_by_id(task_id):
    for task in db.tasks:
        if task.get('id') == task_id:
            return task


def update_task_fields(updated_task_data, task):
    for field in ['title', 'description', 'due_date']:
        if field in updated_task_data:
            task[field] = updated_task_data[field]


def delete_task_by_id(task_id):
    index = None
    for i in range(len(db.tasks)):
        if db.tasks[i].get('id') == task_id:
            index = i
            break
    return index

def search_by_text(text):
    return list(filter(lambda task: text in task.get('title') or text in task.get('description'), db.tasks))