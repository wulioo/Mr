# -*- codeing = utf-8 -*-
# @Time : 2020/12/12 6:02 下午

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# --初始化一个db对象，需要放在config后面
db = SQLAlchemy(app)

book_tag = db.Table(
    'book_tag',
    db.Column('book_id', db.Integer, db.ForeignKey('bookss.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('shelfing.id'), primary_key=True)
)


class Book(db.Model):
    __tablename__ = 'bookss'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    tags = db.relationship('Shelfing', secondary=book_tag, backref=db.backref('books'))


class Shelfing(db.Model):
    __tablename__ = 'shelfing'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(50), nullable=False)


db.create_all()


@app.route('/add')
def add():
    book1 = Book(name='java')
    book2 = Book(name='python')
    book3 = Book(name='c++')
    tag1 = Shelfing(tag='计算机')
    tag2 = Shelfing(tag='技术')
    tag3 = Shelfing(tag='技术')
    book1.tags.append(tag3)
    book1.tags.append(tag2)
    book2.tags.append(tag3)
    book3.tags.append(tag1)
    db.session.add_all([book1, book2, book3, tag1, tag2, tag3])
    db.session.commit()
    return 'sussec'


@app.route('/select')
def selecet():
    book = Book.query.filter(Book.name == 'java').first()


if __name__ == '__main__':
    app.run()
