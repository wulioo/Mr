from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from apps.user.moder import User
from apps import create_app
from flask_script import Manager

from exts import db

app = create_app()
manager = Manager(app=app)

# -- 命令工具
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    print('初始化')


if __name__ == '__main__':
    manager.run()
