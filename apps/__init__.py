# -*- codeing = utf-8 -*-
# @Time : 2020/12/10 2:56 下午
from flask import Flask


import settings
from apps.user.view import user_bp


def create_app():
    app = Flask(__name__, template_folder='../templates',static_folder='../static')
    app.config.from_object(settings)

    #加载蓝图
    app.register_blueprint(user_bp)

    return app




