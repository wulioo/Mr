# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 3:15 下午
# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 9:35 上午

from flask import Flask, request, Response
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def set_cookie():
    '''
    想让cookie存在一段时间，就要为expires属性设置一个过期日期，该属性
    已经被Max-age取代，max-age用秒来设置cookie生存期
    :return:
    '''
    resp = Response('cookie')
    # --服务器respone返回一个cookie
    # resp.set_cookie('name', 'zhangsan')
    # --以表单的形式返回一个cookie
    resp.headers['Set-cookie'] = "username=lisi;Expires=SUN,Max-Age=3600;path=/"
    # --删除一个cookie
    resp.delete_cookie('usename')
    return resp


@app.route('/getCookie')
def getCookie():
    # --get获取cookie
    username = None

    if request.cookies.get('username'):
        username = request.cookies.get('username')

    return username


if __name__ == '__main__':
    app.run(host='0.0.0.0')
