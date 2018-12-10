#!/usr/bin/env python
import os
from app import create_app, db
from app import models
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_msearch import Search
import pymysql

pymysql.install_as_MySQLdb()


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
search = Search()
search.init_app(app)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()