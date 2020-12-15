# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 10:08 上午
# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 9:35 上午

from flask import Flask, request,render_template
from werkzeug.utils import secure_filename

from config import DevelopmentConfig
import os
from os import path

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/upload', methods=['POST', 'GET'])
def upload():

        if request.method == 'GET':
            return render_template('upload.html')
        else:
            # --获取文件流
            if not os.path.exists('static/uploads'):
                os.mkdir('static/uploads')
            f = request.files['file']
            # --secure_filename过滤文件文件名
            filename = secure_filename(f.filename)
            # --路径拼接 保存文件
            f.save(path.join('static/uploads', filename))
            print(app.root_path)
            return 'sussec'


if __name__ == '__main__':
    app.run(DEBUG=True)
