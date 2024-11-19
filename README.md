# Task Management System
## Setup
### Clone the repository

```
git clone https://github.com/VedaSagar2004/Wellness360_Case_Study
cd Wellness360_Case_Study
```
### Install requirements

```
virtualenv env --python=python3.8
.\env\Scripts\activate
pip install -r requirements.txt
```
### Run the application

```
python app.py
```
### Run tests
```
pytest tests/
```

## API Endpoints
### Authentication
### POST /auth/register
```
payload:
{
    "username": "your username",
    "password": "your password"
}
response:
{
    "mesage": "User registered successfully"
}
```
### POST /auth/login
```
payload:
{
    "username": "your username",
    "password": "your password"
}
response:
{
    "token": <jwt_token>
}
```
### Tasks

### GET /tasks
List all tasks
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

response:
[
  {
    'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
    'description': 'some description',
    'due_date': '19-11-2024',
    'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
    'status': 'pending',
    'title': 'some title',
    'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
  },
  {
    'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
    'description': 'some description',
    'due_date': '19-11-2024',
    'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
    'status': 'completed',
    'title': 'some title',
    'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
  },
]
```
### POST /tasks
Create an assignment
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

payload:
{
  "title": "some title",
  "description": "some description"
}
response:
{
  'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
  'description': 'some description',
  'due_date': '',
  'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
  'status': 'pending',
  'title': 'some title',
  'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
}
```
### GET /tasks/<task_id>
Get task by id
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

response:
{
  'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
  'description': 'some description',
  'due_date': '',
  'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
  'status': 'pending',
  'title': 'some title',
  'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
}
```
### PUT /tasks/<task_id>
Update a task by id
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

payload:
{
  "title": "some updated title",
  "description": "some updated description"
}

response:
{
  'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
  'description': 'some updated description',
  'due_date': '',
  'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
  'status': 'pending',
  'title': 'some updated title',
  'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
}
```
### DELETE /tasks/<task_id>
Delete a task by id
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

#deleted task
response:
{
  'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
  'description': 'some updated description',
  'due_date': '',
  'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
  'status': 'pending',
  'title': 'some updated title',
  'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
}
```
### PATCH /tasks/<task_id>/complete
Marks a task as complete
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

response:
{
  'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
  'description': 'some updated description',
  'due_date': '',
  'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
  'status': 'complete',
  'title': 'some updated title',
  'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
}
```
### PATCH /tasks/<task_id>/progress
Marks a task as in_progress
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

response:
{
  'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
  'description': 'some updated description',
  'due_date': '',
  'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
  'status': 'in_progress',
  'title': 'some updated title',
  'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
}
```
### GET tasks/status/<task_status>
List all tasks by task status
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

response:
[
  {
    'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
    'description': 'some description',
    'due_date': '19-11-2024',
    'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
    'status': '<task_status',
    'title': 'some title',
    'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
  },
  {
    'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
    'description': 'some description',
    'due_date': '19-11-2024',
    'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
    'status': '<task_status',
    'title': 'some title',
    'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
  },
]
```
### GET tasks/search/<text_to_search>
Search text in Title and Description
```
headers:
{'Authorization': 'Bearer <your_jwt_token>'}

response:
[
  {
    'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
    'description': 'some description',
    'due_date': '19-11-2024',
    'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
    'status': '<task_status',
    'title': 'some title',
    'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
  },
  {
    'created_at': 'Mon, 18 Nov 2024 10:47:01 GMT',
    'description': 'some description',
    'due_date': '19-11-2024',
    'id': '83253727-2fd2-43a4-b3aa-6b723d5cdb34',
    'status': '<task_status',
    'title': 'some title',
    'updated_at': 'Mon, 18 Nov 2024 10:47:01 GMT'
  },
]
```
