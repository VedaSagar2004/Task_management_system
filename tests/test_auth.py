from app.database.datastore import db
from app.common.constants import TestTasks
from app.common.constants import StatusCodes



def test_user_already_exists(client):
    db.users.extend(TestTasks.test_multiple_users)
    response = client.post(
        '/auth/register',
        json = TestTasks.test_single_user1
    )
    assert response.status_code == StatusCodes.BAD_REQUEST


def test_invalid_credentials(client):
    db.users.extend(TestTasks.test_multiple_users)
    response = client.post(
        '/auth/login',
        json = TestTasks.test_single_user2
    )
    assert response.status_code == StatusCodes.UNAUTHORIZED


def test_register_user(client):
    response = client.post(
        '/auth/register',
        json = TestTasks.test_single_user1
    )
    assert db.users[-1].get('username') == TestTasks.test_single_user1.get('username')
    assert response.status_code == StatusCodes.CREATED


def test_login_user(client):
    db.users.extend(TestTasks.test_multiple_users)
    response = client.post(
        '/auth/login',
        json = TestTasks.test_single_user1
    )
    assert response.status_code == StatusCodes.OK