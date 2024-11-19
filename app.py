# from flask import Flask, jsonify
# from tasks import tasks_bp, auth_bp
# from config import StatusCodes
# app = Flask(__name__)

# # Register the tasks blueprint
# app.register_blueprint(tasks_bp, url_prefix='/tasks')
# app.register_blueprint(auth_bp, url_prefix='/auth')

# @app.route('/')
# def home():
#     return {"message": "Welcome to the Task API"}, 200

# @app.errorhandler(Exception)
# def handle_exception(e):
#     return jsonify({'error': str(e)}), StatusCodes.INTERNAL_SERVER_ERROR

# if __name__ == '__main__':
#     app.run(debug=True)

from app import app

if __name__ == '__main__':
    app.run(debug=True)
