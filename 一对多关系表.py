# -*- codeing = utf-8 -*-
# @Time : 2020/12/12 11:23 上午

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# --初始化一个db对象，需要放在config后面
db = SQLAlchemy(app)


class Writer(db.Model):
    __tablename__ = 'writer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    # --建立模型关系
    # books = db.relationship('Book', backref='writers')


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    publishing_office = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(50), nullable=False)
    writer_id = db.Column(db.Integer, db.ForeignKey('writer.id'))


db.create_all()


@app.route('/add')
def add():
    user1 = Writer(name='郑代辉')
    user2 = Writer(name='帅帅辉')
    db.session.add(user1)
    db.session.add(user2)
    book1 = Book(title='名师', publishing_office='清华大学', isbn='12123123', writer_id=1)
    book2 = Book(title='ios开发', publishing_office='清华大学', isbn='12123123', writer_id=2)
    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()
    return 'yes'


@app.route('/select')
def select():
    writer = Writer.query.filter(Writer.id == '1').first()
    # book = writer.books
    # print(book[0].title)
    a=Book.query.filter(Book.id == '1').first()
    print(a)
    # writer = book.writers
    print(writer.name)
    return 'sussecc'


if __name__ == '__main__':
    app.run(host='0.0.0.0', DEBUG=True)
