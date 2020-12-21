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
def create():
    # --创建一个数据
    db.create_all()
    print('初始化')


# 为user表添加数据
@manager.option('-u', '--username', dest="username")
@manager.option('-p', '--password', dest="password")
@manager.option('-k', '--phone', dest='phone')
def insetDB(username, password, phone):
    user = User(username=username, password=password, phone=phone)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
