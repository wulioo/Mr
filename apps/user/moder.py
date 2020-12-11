# -*- codeing = utf-8 -*-
# @Time : 2020/12/10 3:25 下午

from loguru import logger

class User:
    def __init__(self,name,password,phone=None):
        self.name = name
        self.password = password
        self.phone = phone

    def __str__(self):
        return self.name