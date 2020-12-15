# -*- codeing = utf-8 -*-
# @Time : 2020/12/12 12:26 上午
# import os
from os import urandom
from datetime import timedelta
class Config:
    DEBUG = True
    host = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    ENV = 'development'
    # --设置session24位加密
    SECRET_KEY = urandom(24)
    # --配置session3天有效果
    PERMANENT_SESSION_LIFETIME=timedelta(days=3)




class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
