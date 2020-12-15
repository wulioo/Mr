# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 4:10 下午

from flask import Flask
import app蓝图.news, app蓝图.produt

app = Flask(__name__)


@app.route('/')
def hello_word():
    print('b')
    return 'hello word'


app.register_blueprint(app蓝图.news.new_list)
app.register_blueprint(app蓝图.produt.product_list)

if __name__ == '__main__':

    app.run(DEBUG=True)
