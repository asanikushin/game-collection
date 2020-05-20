from .check_id import check_id
from .upload import upload_file

from flask import Blueprint

game_file = Blueprint("games", __name__)

game_file.add_url_rule("/", "upload_file", upload_file, methods=["POST"])
game_file.add_url_rule("/", "check_id", check_id, methods=["GET"])
