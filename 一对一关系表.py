# -*- codeing = utf-8 -*-
# @Time : 2020/12/12 12:42 上午

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# --初始化一个db对象，需要放在config后面
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)


class Lib_card(db.Model):
    '''
    relationship 关联
    ForeignKey 为carb表关联user父表id字段，card表拥有user_id，也就是创建一个外键
    relationship 关联User表 backref为user表添加了隐藏字段cards cards拥有表的所有字段
    uselist=False 表示 一对一关系
    '''
    __tablename__ = 'lib_card'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_id = db.Column(db.Integer, nullable=False)
    papers_type = db.Column(db.String(50), nullable=False)
    borrow_reg_time = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users1 = db.relationship('User', backref=db.backref('cards1', uselist=False))


db.create_all()


@app.route('/add')
def add():
    user1 = User(username='张三', password='123123', phone='11111111', email='100@qq.com')
    user2 = User(username='李四', password='234567', phone='11111111', email='100@qq.com')
    db.session.add(user1)
    db.session.add(user2)
    card1 = Lib_card(card_id=18001, papers_type='bb', user_id=1)
    card2 = Lib_card(card_id=18002, papers_type='bb', user_id=2)
    db.session.add(card1)
    db.session.add(card2)
    db.session.commit()
    return 'success'


@app.route('/select')
def select():
    '''
    多表关联
    :return:
    '''
    a = User.query.filter(User.username == '张三').first()
    b = Lib_card.query.filter(Lib_card.card_id == '18001').first()
    # art = user.cards
    # print(art.card_id)
    #
    # card = Lib_card.query.filter(Lib_card.card_id == '18001').first()
    # user = card.users
    # print(user.username)
    return 'sessce'


if __name__ == '__main__':
    app.run(host='0.0.0.0', DEBUG=True)
