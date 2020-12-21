# -*- codeing = utf-8 -*-
# @Time : 2020/12/10 3:16 下午

from flask import Blueprint, redirect
from flask import request, render_template

from apps.user.moder import User

user_bp = Blueprint('user', __name__)

users = []


@user_bp.route('/')
def user_center():
    return render_template('user/show.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # --获取post提交数据
        name = request.form.get('name')
        pswd = request.form.get('password')
        phone = request.form.get('phone')
        repswd = request.form.get('repassword')
        if pswd == repswd:
            for user in users:
                if user.name == name:
                    return render_template('user/register.html', msg='用户名已经存在')
            user = User(name, pswd, phone)
            users.append(user)
            return redirect('/')
    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return '用户登录'


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return '用户退出'


@user_bp.route('/del')
def del_user():
    name = request.args.get('name')
    for user in users:
        if user.name == name:
            users.remove(user)
            return redirect('/')
    else:
        return "error"


@user_bp.route('/update', methods=['GET', 'POST'],endpoint='update')
def update_user():
    if request.method == 'POST':
        realname = request.form.get('realname')
        name = request.form.get('name')
        pswd = request.form.get('password')
        phone = request.form.get('phone')
        for user in users:
            if user.name == realname:
                user.name = name
                user.phone = phone
                return 'succsse'
    else:
        name = request.args.get('name')
        for user in users:
            if user.name == name:
                return render_template('user/update.html', user=user)
