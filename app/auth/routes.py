from app.auth import auth_blueprint
from flask import request, jsonify
from app.database.datastore import db
from app.common.constants import StatusCodes, ErrorMessages, Messages, JWTSecret
import jwt
import bcrypt


@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': ErrorMessages.USERNAME_PASSWORD_REQUIRED}), StatusCodes.BAD_REQUEST
    for user in db.users:
        if user.get('username') == data.get('username'):
            return jsonify({'error': ErrorMessages.USER_ALREADY_EXISTS}), StatusCodes.BAD_REQUEST
    hashed_password = bcrypt.hashpw(data.get('password').encode('utf-8'), bcrypt.gensalt())
    db.users.append({'username': data.get('username'), 'password': hashed_password.decode('utf-8')})
    return jsonify({'message': Messages.USER_REGISTERED, 'hash': hashed_password.decode('utf-8')}), StatusCodes.CREATED


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': ErrorMessages.USERNAME_PASSWORD_REQUIRED}), StatusCodes.BAD_REQUEST
    user = None
    for registered_user in db.users:
        if registered_user.get('username') == data.get('username') and bcrypt.checkpw(data.get('password').encode('utf-8'), registered_user.get('password').encode('utf-8'),):
            user = registered_user
    if not user:
        return jsonify({'error': ErrorMessages.INVALID_CREDENTIALS}), StatusCodes.UNAUTHORIZED
    token = jwt.encode(user, JWTSecret.jwt_secret, algorithm='HS256')
    return jsonify({'token': token}), StatusCodes.OK