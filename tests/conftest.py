import pytest
from app.database.datastore import db
from app import app
from app.common.constants import TestTasks

@pytest.fixture
def client():
    return app.test_client()

# clears tasks and users before and after the test
@pytest.fixture(autouse=True, scope='function')
def reset_tasks():
    db.clear_all() 
    yield
    db.clear_all()



@pytest.fixture
def auth_headers():
    headers = {
        'Authorization': f"Bearer {TestTasks.test_token}",
        'Content-Type': 'application/json' 
    }
    return headers




