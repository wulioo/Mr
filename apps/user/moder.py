# -*- codeing = utf-8 -*-
# @Time : 2020/12/10 3:25 下午

"""
ORM 类 ---》表
类对象  ---》表中的一条记录
"""
from datetime import datetime

from exts import db


class User(db.Model):
    # --db,Column（类型）映射表中的列
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # --主键 自增
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)  # --唯一约束
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username
