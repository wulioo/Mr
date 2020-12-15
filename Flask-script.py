# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 9:35 上午

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
manager = Manager(app)


@manager.command
def init():
    print('hell,worid')


@manager.option('-n', '--name', dest='name', default='world')
@manager.option('-u', '--url', dest='url', default='www.csdn.com')
def hello(name, url):
    print('hell', name)
    print(url)


if __name__ == '__main__':
    manager.run()
