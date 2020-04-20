#!/usr/bin/env python

from auth.models.users import User
from utils.constants import UserRole

import os


def add_first_admin(name="admin", password="admin", app=None, db=None):
    os.system("echo try add Admin user")
    with app.app_context():
        if User.query.filter(User.email == name).first() is None:
            admin = User(email=name, confirmed=True)
            admin.set_password(password)
            admin.set_role(UserRole.ADMIN)

            db.session.add(admin)
            db.session.commit()
