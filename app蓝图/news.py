# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 4:09 下午

from flask import Blueprint

new_list = Blueprint('news', __name__)

@new_list.route('/news')
def news():
    return '新闻模块'
