from flask import request, jsonify
from functools import wraps
from app.common.constants import ErrorMessages, StatusCodes, JWTSecret
import jwt
from app.database.datastore import db

def require_auth(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer'):
            return jsonify({'error': ErrorMessages.UNAUTHORIZED}), StatusCodes.UNAUTHORIZED
        token = token.split()[1]
        user_found = False
        for user in db.users:
            if user.get('username') == jwt.decode(token, JWTSecret.jwt_secret, algorithms=['HS256']).get('username'):
                user_found = True
                break
        if not user_found:
            return jsonify({'error': ErrorMessages.INVALID_CREDENTIALS}), StatusCodes.UNAUTHORIZED
        return f(*args, **kwargs)
    return wrapped