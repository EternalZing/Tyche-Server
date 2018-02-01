'''ha '''
# pylint: disable=E1101

from tyche import db


class User(db.Model):
    ''' user model'''
    __tablename__ = 't_user'

    userid = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(16))
    user_password = db.Column(db.String(18), nullable=False)
    username = db.Column(db.String(19))
    user_email = db.Column(db.String(25))

    def __init__(self, username, password, email, utype):
        self.username = username
        self.user_password = password
        self.email = email
        self.user_type = utype

    def __repr__(self):
        return '<User %r>' % self.username


class Rule(db.Model):
    __tablename__ = 't_rules'
    ru_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    ru_name = db.Column(db.Integer)
    ru_father = db.Column(db.Integer)
    ru_short = db.Column(db.String(128))
    ru_file_add = db.Column(db.String(128))
