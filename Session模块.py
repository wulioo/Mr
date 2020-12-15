# -*- coding:utf-8 -*-
# @Time : 2020/12/14 4:58 下午

from flask import Flask, request, Response, session
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def set_session():
    '''
    设置session 必须把session加密
    :return:
    '''
    session['username'] = 'zhangsan'
    # --设置session过期时间
    session.permanent = True
    return 'success'


# --获取session
@app.route('/getSession')
def getSession():
    username = session.get('username')
    # -- 删除某个session
    # session.pop('username')
    # --清空session
    # session.clear

    return username or 'session'

if __name__ == '__main__':
    app.run()
