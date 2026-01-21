from flask import Blueprint, jsonify
from services.repo_service.service import RepoService
from services.repo_service.controllers.repo_controller import RepoController

repo_bp = Blueprint("repo_service", __name__)
controller = RepoController(RepoService())

@repo_bp.route("/api/repos/<username>")
def get_repos(username):
    return jsonify(controller.fetch_repos(username))
