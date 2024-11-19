from flask import Flask, jsonify
from app.tasks import tasks_blueprint
from app.auth import auth_blueprint
from app.common.constants import StatusCodes

# Register the tasks blueprint
def create_app():
    app = Flask(__name__)   
    app.register_blueprint(tasks_blueprint, url_prefix='/tasks')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({'error': str(e)}), StatusCodes.INTERNAL_SERVER_ERROR

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)