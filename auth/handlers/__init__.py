from .singup import register_user
from .singin import sing_in
from .refresh import refresh_tokens
from .validate import validate
from .confirm import confirm
from .roles import change_role

from flask import Blueprint

auth = Blueprint("auth", __name__)

auth.add_url_rule("/register", "register", register_user, methods=['POST'])
auth.add_url_rule("/singin", "sing_in", sing_in, methods=['POST'])

auth.add_url_rule("/refresh", "refresh", refresh_tokens, methods=['POST'])
auth.add_url_rule("/validate", "validate", validate, methods=['POST'])

auth.add_url_rule("/confirm/<token>", "confirm", confirm, methods=['GET'])
auth.add_url_rule("/change_role", "change_role", change_role, methods=['POST'])
