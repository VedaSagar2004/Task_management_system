class StatusCodes:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    UNAUTHORIZED = 401


class TaskStatus:
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class ErrorMessages:
    TASK_NOT_FOUND = "Task not found"
    ALREADY_COMPLETED = "Task already completed"
    INVALID_JSON = "Request must be in JSON and not be empty"
    MISSING_TITLE = "Title is required"
    INVALID_DATE_FORMAT = "Due date must be in the format DD-MM-YYYY"
    INVALID_FIELD_TYPE = "{} must be a {}"
    USERNAME_PASSWORD_REQUIRED = "username and password are required"
    USER_ALREADY_EXISTS = "user already exists"
    INVALID_CREDENTIALS = "invalid credentials"
    UNAUTHORIZED = "unauthorized"
    INVALID_STATUS = "Invalid task status"
    ALREADY_IN_PROGRESS = "Task already in progress"

class Messages:
    USER_REGISTERED = "user registered successfully"
    USER_LOGGED_IN = "user logged in successfully"


class JWTSecret:
    jwt_secret = "my_secret"


class TestConfig:
    TESTING = True
    DEBUG = False
    DATABASE = []


class TestTasks:
    test_tasks = [
        {
            "created_at": "Mon, 18 Nov 2024 10:47:01 GMT",
            "description": "description1",
            "due_date": "19-11-2024",
            "id": "83253727-2fd2-43a4-b3aa-6b723d5cdb34",
            "status": "pending",
            "title": "task1",
            "updated_at": "Mon, 18 Nov 2024 10:47:01 GMT"
        },
        {
            "created_at": "Mon, 18 Nov 2024 10:47:09 GMT",
            "description": "description2",
            "due_date": "19-11-2024",
            "id": "765da060-141d-4e19-9a2f-45590b167eab",
            "status": "pending",
            "title": "task2",
            "updated_at": "Mon, 18 Nov 2024 10:47:09 GMT"
        },
        {
            "created_at": "Mon, 18 Nov 2024 10:47:17 GMT",
            "description": "description3",
            "due_date": "19-11-2024",
            "id": "a5b73ac3-940c-4a76-9163-752cc4d2341b",
            "status": "pending",
            "title": "task3",
            "updated_at": "Mon, 18 Nov 2024 10:47:17 GMT"
        },
        {
            "created_at": "Mon, 18 Nov 2024 10:47:17 GMT",
            "description": "description3",
            "due_date": "19-11-2024",
            "id": "a5b73ac3-940c-4a76-9163-752cc4d2341b",
            "status": "in_progress",
            "title": "task3",
            "updated_at": "Mon, 18 Nov 2024 10:47:17 GMT"
        },
        {
            "created_at": "Mon, 18 Nov 2024 10:47:17 GMT",
            "description": "description3",
            "due_date": "19-11-2024",
            "id": "a5b73ac3-940c-4a76-9163-752cc4d2341b",
            "status": "completed",
            "title": "task3",
            "updated_at": "Mon, 18 Nov 2024 10:47:17 GMT"
        }
    ]
    test_multiple_users = [
        {
            "username": "Veda",
            "password": "1234"
        },
        {
            "username": "Tazo",
            "password": "$2b$12$Y9sdwbb.XIG3ONDl7jYjAuvedTMvFO//a7CKHD0NoxRv2b8fs9TbG"
        }
    ]
    test_single_user1 ={
        "username": "Tazo",
        "password": "1234"
    }
    test_single_user2 ={
        "username": "Tazo",
        "password": "12345"
    }
    test_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlRhem8iLCJwYXNzd29yZCI6IiQyYiQxMiRZOXNkd2JiLlhJRzNPTkRsN2pZakF1dmVkVE12Rk8vL2E3Q0tIRDBOb3hSdjJiOGZzOVRiRyJ9.43Hu5Y3CDthdnnxBYkD1-6D87P3fnOhdTH7nzyaGnps"
    task_id = "765da060-141d-4e19-9a2f-45590b167eab"
    create_task = {
        "title": "task1",
        "description": "description1",
        "due_date": "19-11-2024"
    }
    update_task = {
        "title": "updated_title",
        "description": "updated_description"
    }
    missing_title_task = {
        "description": "missing title"
    }