#!/usr/bin/env python
from auth import create_app, db

from auth.fill_data import add_first_admin
from auth.rpc_server import create_server

from flask_script import Manager, Shell
from flask_migrate import MigrateCommand


def make_shell_context():
    return dict(app=app, db=db)


app = create_app()
manager = Manager(app)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    add_first_admin(app=app, db=db)
    rpc_server = create_server(cur_app=app)
    rpc_server.start()
    manager.run()
