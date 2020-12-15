# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 4:10 下午

from flask import Blueprint

product_list = Blueprint('products', __name__)


@product_list.route('/products')
def product():
    return '产品模块'
