# pylint: disable=E1101
from flask import request
from tyche.models import User
from tyche import db
from . import user


@user.route("/users/Register", methods=['POST', 'GET'])
def register_user():
    '''doc string'''
    new = User(request.form['username'], request.form['password'],
               request.form['email'], 'normal')
    print("username is %", new)
    db.session.add(new)
    db.session.commit()
    return 'register complete'
