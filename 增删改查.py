# -*- codeing = utf-8 -*-
# @Time : 2020/12/12 12:23 上午
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# --初始化一个db对象，需要放在config后面
db = SQLAlchemy(app)


# --建立表
class Book(db.Model):
    # --对应数据库表的别名
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)


# --创建数据库表--测试数据库是否连接成功
# db.create_all()
# --book表中添加数据
# book1 = Book(id='004', title='vv')
# db.session.add(book1)
# db.session.commit()
# -------------

# --添加数据到路由
@app.route('/add')
def add():
    '''
    url视图访问add即可添加数据
    :return:
    '''
    book1 = Book(title='vv')
    book2 = Book(title='vv')
    book3 = Book(title='vv')
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()
    return 'sussec'


# --数据查询
@app.route('/select')
def select():
    '''
    query是从db.Model中继承来的，
    query.filter(Book.id='xx')为过滤条件，
    first()取出查询结果的第一条数据
    all()查询符合条件所有
    :return: 
    '''
    result = Book.query.filter(Book.id == '2').first()
    result1 = Book.query.filter(Book.title == 'vv').all()
    print(result1)
    print(result.title)
    for books in result1:
        print(books)
        print(books.title)
    return 'sess'


@app.route('/edit')
def edit():
    '''
    1.数据修改
    :return:
    '''
    book = Book.query.filter(Book.id == '1').first()
    book.title = 'shuaishuai'
    db.session.commit()
    return 'success'


@app.route('/delete')
def delete():
    book = Book.query.filter(Book.id == '1').first()
    db.session.delete(book)
    db.session.commit()
    return 'success'


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(host='0.0.0.0', DEBUG=True)
