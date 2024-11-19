from flask import request, jsonify
from datetime import datetime
from app.tasks.utils import validate_task_data, find_task_by_id, update_task_fields, delete_task_by_id, search_by_text
from app.auth.utils import require_auth
from app.database.datastore import db
from app.tasks import tasks_blueprint
from app.common.constants import StatusCodes, TaskStatus, ErrorMessages
from uuid import uuid4
import jwt


@tasks_blueprint.route('', methods=['GET'])
@require_auth
def get_tasks():
    return jsonify(db.tasks), StatusCodes.OK


@tasks_blueprint.route('', methods=['POST'])
@require_auth
def create_task():
    new_task_data = request.get_json()
    is_valid, error_message = validate_task_data(new_task_data)
    if not is_valid:
        return jsonify({'error': error_message}), StatusCodes.BAD_REQUEST
    new_task = {
        "id": str(uuid4()),
        "title": new_task_data.get('title'),
        "description": new_task_data.get('description', ""),
        "due_date": new_task_data.get('due_date', ""),
        "status": TaskStatus.PENDING,
        "created_at": str(datetime.now()),
        "updated_at": str(datetime.now())
    }

    db.tasks.append(new_task)
    return jsonify(new_task), StatusCodes.CREATED


@tasks_blueprint.route('/<string:task_id>', methods=['GET'])
@require_auth
def get_task_by_id(task_id):
    task = find_task_by_id(task_id)
    if task:
        return jsonify(task), StatusCodes.OK
    else:
        return jsonify({'error': ErrorMessages.TASK_NOT_FOUND}), StatusCodes.NOT_FOUND


@tasks_blueprint.route('/<string:task_id>', methods=['PUT'])
@require_auth
def update_task(task_id):
    updated_task_data = request.get_json()
    is_valid, error_message = validate_task_data(updated_task_data, required_title=False)
    if not is_valid:
        return jsonify({'error': error_message}), StatusCodes.BAD_REQUEST
    task = find_task_by_id(task_id)
    if not task:
        return jsonify({'error': ErrorMessages.TASK_NOT_FOUND}), StatusCodes.NOT_FOUND
    update_task_fields(updated_task_data, task)
    task['updated_at'] = str(datetime.now())
    return jsonify(task), StatusCodes.OK


@tasks_blueprint.route('/<string:task_id>', methods=['DELETE'])
@require_auth
def delete_task(task_id):
    index = delete_task_by_id(task_id)
    if index is None:
        return jsonify({'error': ErrorMessages.TASK_NOT_FOUND}), StatusCodes.NOT_FOUND
    deleted_task = db.tasks.pop(index)
    return jsonify(deleted_task), StatusCodes.OK


@tasks_blueprint.route('/<string:task_id>/complete', methods=['PATCH'])
@require_auth
def mark_task_complete(task_id):
    task = find_task_by_id(task_id)
    if not task:
        return jsonify({'error': ErrorMessages.TASK_NOT_FOUND}), StatusCodes.NOT_FOUND
    if task.get('status') == TaskStatus.COMPLETED:
        return jsonify({'message': ErrorMessages.ALREADY_COMPLETED}), StatusCodes.OK
    task['status'] = TaskStatus.COMPLETED
    task['updated_at'] = str(datetime.now())
    return jsonify(task), StatusCodes.OK


@tasks_blueprint.route('/status/<string:task_status>', methods=['GET'])
@require_auth
def get_tasks_by_status(task_status):
    if task_status not in [TaskStatus.COMPLETED, TaskStatus.IN_PROGRESS, TaskStatus.PENDING]:
        return jsonify({'error': ErrorMessages.INVALID_STATUS}), StatusCodes.BAD_REQUEST
    result = filter(lambda task: task.get('status') == task_status, db.tasks)
    return jsonify(list(result)), StatusCodes.OK


@tasks_blueprint.route('/<string:task_id>/progress', methods=['PATCH'])
@require_auth
def mark_task_in_progress(task_id):
    task = find_task_by_id(task_id)
    if not task:
        return jsonify({'error': ErrorMessages.TASK_NOT_FOUND}), StatusCodes.NOT_FOUND
    if task.get('status') == TaskStatus.IN_PROGRESS:
        return jsonify({'message': ErrorMessages.ALREADY_IN_PROGRESS}), StatusCodes.OK
    task['status'] = TaskStatus.IN_PROGRESS
    task['updated_at'] = str(datetime.now())
    return jsonify(task), StatusCodes.OK


@tasks_blueprint.route('/search//<string:text>', methods=['GET'])
@require_auth
def search_in_title_and_description(text):
    result = search_by_text(text)
    return jsonify(result), StatusCodes.OK