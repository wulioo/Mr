# -*- codeing = utf-8 -*-
# @Time : 2020/12/10 2:56 下午
from flask import Flask
from settings import DevelopmentConfig
from apps.user.view import user_bp
from exts import db


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)  # --将db对象与app进行了关联
    # --注册蓝图
    app.register_blueprint(user_bp)

    return app
