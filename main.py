
from flask import Flask, Response, request, render_template
import socket
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    """
    查询本机ip地址
    :return: ip
    """

    return render_template('index.html')  # 返回的Response对象

@app.errorhandler(404)
def page not found(e):
    return rendern_template('404.html'),404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9100)
