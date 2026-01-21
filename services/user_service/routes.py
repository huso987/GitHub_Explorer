from flask import Blueprint, jsonify
from services.user_service.controllers.user_controller import UserController

user_bp = Blueprint("user_service", __name__)
controller = UserController()

@user_bp.route("/api/users/<username>")
def get_user(username):
    return jsonify(controller.fetch_user(username))
