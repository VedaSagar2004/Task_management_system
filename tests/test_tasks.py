import pytest
from app import app
from app.database.datastore import db
from app.common.constants import TestTasks
from app.tasks.utils import find_task_by_id, update_task_fields, search_by_text
from app.common.constants import StatusCodes, TaskStatus
import jwt


def test_title_missing(client, auth_headers):
    db.users.extend(TestTasks.test_multiple_users)
    response = client.post(
        '/tasks',
        json = TestTasks.missing_title_task,
        headers = auth_headers
    )
    assert response.status_code == StatusCodes.BAD_REQUEST


def test_task_not_found(client, auth_headers):
    db.users.extend(TestTasks.test_multiple_users)
    db.users.extend(TestTasks.test_tasks)
    response = client.get(
        '/tasks/random_id',
        headers = auth_headers
    )
    assert response.status_code == StatusCodes.NOT_FOUND


def test_get_tasks(client, auth_headers):
    db.tasks.extend(TestTasks.test_tasks)
    db.users.extend(TestTasks.test_multiple_users)
    print(db.users)
    response = client.get(
        '/tasks',
        headers = auth_headers
        )
    print(auth_headers)
    assert db.tasks == response.json
    assert response.status_code == StatusCodes.OK


def test_get_task_by_id(client, auth_headers):
    db.tasks.extend(TestTasks.test_tasks)
    db.users.extend(TestTasks.test_multiple_users)
    response = client.get(
        f'/tasks/{TestTasks.task_id}',
        headers = auth_headers
        )
    print(response.json)
    task = find_task_by_id(TestTasks.task_id)
    assert task == response.json
    assert response.status_code == StatusCodes.OK


def test_create_task(client, auth_headers):
    db.users.extend(TestTasks.test_multiple_users)
    response = client.post(
        '/tasks',
        json = TestTasks.create_task,
        headers = auth_headers
        )
    assert response.status_code == StatusCodes.CREATED


def test_update_task(client, auth_headers):
    db.users.extend(TestTasks.test_multiple_users)
    db.tasks.extend(TestTasks.test_tasks)
    response = client.put(
        f'/tasks/{TestTasks.task_id}',
        json = TestTasks.update_task,
        headers = auth_headers
        )
    task = find_task_by_id(TestTasks.task_id)
    update_task_fields(task, TestTasks.update_task)
    for field in ["title", "description", "due_date"]:
        assert task.get(field) == response.json.get(field)
    assert response.status_code == StatusCodes.OK


def test_delete_task(client, auth_headers):
    db.tasks.extend(TestTasks.test_tasks)
    db.users.extend(TestTasks.test_multiple_users)
    response = client.delete(
        f'/tasks/{TestTasks.task_id}',
        headers = auth_headers
        )
    task = find_task_by_id(TestTasks.task_id)
    assert task == None
    assert response.status_code == StatusCodes.OK


def test_mark_complete(client, auth_headers):
    db.tasks.extend(TestTasks.test_tasks)
    db.users.extend(TestTasks.test_multiple_users)
    response = client.patch(
        f'/tasks/{TestTasks.task_id}/complete',
        headers = auth_headers
        )
    task = find_task_by_id(TestTasks.task_id)
    assert task.get('status') == TaskStatus.COMPLETED
    assert response.status_code == StatusCodes.OK


def test_mark_task_in_progress(client, auth_headers):
    db.tasks.extend(TestTasks.test_tasks)
    db.users.extend(TestTasks.test_multiple_users)
    response = client.patch(
        f'/tasks/{TestTasks.task_id}/progress',
        headers = auth_headers
    )
    task = find_task_by_id(TestTasks.task_id)
    assert task.get('status') == TaskStatus.IN_PROGRESS
    assert response.status_code == StatusCodes.OK


def test_get_tasks_by_status(client, auth_headers):
    db.users.extend(TestTasks.test_multiple_users)
    db.tasks.extend(TestTasks.test_tasks)
    for status in [TaskStatus.COMPLETED, TaskStatus.PENDING, TaskStatus.IN_PROGRESS]:
        response = client.get(
            f'/tasks/status/{status}',
            headers = auth_headers
        )
        for task in response.json:
            assert task.get('status') == status
        assert response.status_code == StatusCodes.OK


def test_get_tasks_by_searching(client, auth_headers):
    db.users.extend(TestTasks.test_multiple_users)
    db.tasks.extend(TestTasks.test_tasks)
    print(db.tasks)
    text = 'u'
    response = client.get(
        f'/tasks/search/{text}',
        headers = auth_headers
    )
    print(response.json, "comp", search_by_text(text))
    assert response.json == search_by_text(text)
    assert response.status_code == StatusCodes.OK