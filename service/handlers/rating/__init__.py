from .addScore import add_score
from .deleteScore import delete_score
from .getScore import get_game_rating, get_user_scores
from .patchScore import patch_score

from flask import Blueprint

rating = Blueprint("rating", __name__)

rating.add_url_rule(
    "/<int:game_id>", "get_game_rating", get_game_rating, methods=["GET"]
)
rating.add_url_rule("/", "add_scores", add_score, methods=["POST"])

rating.add_url_rule(
    "/<int:game_id>", "patch_score", patch_score, methods=["PUT", "PATCH"]
)
rating.add_url_rule("/", "patch_score", patch_score, methods=["PUT", "PATCH"])

rating.add_url_rule("/<int:game_id>", "delete_score", delete_score, methods=["DELETE"])

rating.add_url_rule("/user", "get_ratings", get_user_scores, methods=["GET"])
rating.add_url_rule(
    "/user/<int:user_id>", "get_ratings", get_user_scores, methods=["GET"]
)
