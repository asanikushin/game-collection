from .types import *

from auth.models.users import User, Session
from auth import db
from constants import statuses, UserRole
from utils.checkers import check_email
from utils.queues import send_message

from flask import current_app

import jwt
import json
import secrets
import datetime


class Storage:
    def __init__(self):
        self._db = db

    def add_user(self, email: str, password: str) -> ID_WITH_STATUS:
        if not (email := check_email(email)):
            return None, statuses["user"]["invalidEmail"]

        if self._has_email(email):
            return None, statuses["user"]["emailUsed"]

        user = User(email=email)
        user.set_password(password)
        user.confirmed = False

        self._db.session.add(user)
        self._db.session.commit()

        self._send_confirm_message(user)

        return user.id, statuses["user"]["created"]

    def confirm_user(self, token: str):
        try:
            value = jwt.decode(token, current_app.config["TOKENS_SECRET"], algorithms=['HS256'])
        except (jwt.DecodeError, jwt.ExpiredSignatureError) as err:
            return err, statuses["tokens"]["invalidToken"]
        user = User.query.get(value["id"])
        user.confirmed = True
        self._db.session.commit()

        return "Account confirmed", statuses["user"]["confirmed"]

    def create_session(self, email: str, password: str):
        if not (user := self._get_user(email)):
            return None, None, statuses["user"]["noUser"]

        if not self._check_user_password(user, password):
            return None, None, statuses["user"]["wrongPassword"]

        if not user.confirmed:
            self._send_confirm_message(user)
            return None, None, statuses["user"]["notConfirmed"]

        session = Session(userId=user.id)
        return self._save_session(email, session)

    def update_session(self, refresh_token: str):
        now = datetime.datetime.utcnow()
        session = Session.query.filter(Session.refreshToken == refresh_token).first()

        if session is None:
            return None, None, statuses["tokens"]["noSuchToken"]

        if now > session.refreshTokenExpireAt:
            return None, None, statuses["tokens"]["refreshTokenExpired"]

        user = User.query.get(session.userId)
        new_session = Session(userId=user.id)
        response = self._save_session(user.email, new_session)

        self._delete_session(session)
        return response

    @staticmethod
    def check_token(access_token: str):
        try:
            value = jwt.decode(access_token, current_app.config["TOKENS_SECRET"], algorithms=['HS256'])
        except jwt.ExpiredSignatureError as err:
            return err, statuses["tokens"]["accessTokenExpired"]
        except jwt.DecodeError as err:
            return err, statuses["tokens"]["invalidToken"]
        session_id = value["session"]
        session: Session = Session.query.get(session_id)
        if session is None:
            return "Related session was removed", statuses["tokens"]["invalidToken"]
        user_id = session.userId
        result = dict()
        result["session"] = session.id
        result["role"] = User.query.get(user_id).get_role()
        result["user_id"] = user_id
        result["email"] = value["email"]

        return result, statuses["tokens"]["accessOk"]

    def change_role(self, admin_token: TOKEN, user_id: ID_TYPE, role):
        admin, status = self.check_token(admin_token)
        if status != statuses["tokens"]["accessOk"]:
            return statuses["tokens"]["invalidToken"]
        if admin["role"] != UserRole.ADMIN.value:
            return statuses["user"]["requestNotAllowed"]

        user = User.query.get(user_id)
        user.set_role(role)
        self._db.session.commit()
        return statuses["user"]["roleChanged"]

    @staticmethod
    def _has_email(email: str) -> bool:
        return User.query.filter(User.email == email).first() is not None

    @staticmethod
    def _get_user(email: str) -> User:
        return User.query.filter(User.email == email).first()

    @staticmethod
    def _check_user_password(user: User, password: str) -> bool:
        return user.check_password(password) if user else False

    @staticmethod
    def _create_confirm_link(user: User, time=datetime.datetime.utcnow()):
        token = str(jwt.encode(
            {"id": user.id, "exp": time + current_app.config["ACCESS_TOKEN_EXPIRATION"]},
            current_app.config["TOKENS_SECRET"]))[2:-1]
        return f"{current_app.config['CONFIRM_URL']}/confirm/{token}"

    @staticmethod
    def _send_confirm_message(user: User):
        send_message(current_app.config["RABBITMQ"], current_app.config["QUEUE"], json.dumps(
            dict(email=user.email, text=f"To confirm go to {Storage._create_confirm_link(user)}",
                 subject="Conformation email")))

    @staticmethod
    def _create_tokens(email: str, session: Session, time=datetime.datetime.utcnow()):
        refresh_token = secrets.token_hex(64)
        access_token = str(jwt.encode(
            {"email": email, "session": session.id, "user_id": session.userId,
             "exp": time + current_app.config["ACCESS_TOKEN_EXPIRATION"]},
            current_app.config["TOKENS_SECRET"]))[2:-1]

        return access_token, refresh_token

    def _save_session(self, email: str, session: Session):
        self._db.session.add(session)
        self._db.session.commit()

        now = datetime.datetime.utcnow()
        access_token, refresh_token = self._create_tokens(email, session, now)
        session.refreshToken = refresh_token
        session.refreshTokenExpireAt = now + current_app.config["REFRESH_TOKEN_EXPIRATION"]
        self._db.session.commit()
        return access_token, refresh_token, statuses["tokens"]["created"]

    def _delete_session(self, session: Session):
        self._db.session.delete(session)
        self._db.session.commit()
