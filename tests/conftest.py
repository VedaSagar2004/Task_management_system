import pytest
from app.database.datastore import db
from app import app
from app.common.constants import TestTasks

@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture(autouse=True, scope='function')
def reset_tasks():
    # original_tasks = db.tasks.copy()
    # original_users = db.users.copy()
    
    # Clear all data
    db.clear_all()
    
    yield
    
    # Clear and reset to original state
    db.clear_all()
    # db.tasks.extend(original_tasks)
    # db.users.extend(original_users)


@pytest.fixture
def auth_headers():
    headers = {
        'Authorization': f"Bearer {TestTasks.test_token}",
        'Content-Type': 'application/json' 
    }
    return headers




