from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    UserCode = db.Column(db.String(64), unique=True, index=True)
    Password = db.Column(db.String(128))

    def __init__(self, UserCode=None, Password=None):
        self.UserCode = UserCode
        self.Password = Password

    def __repr__(self):
        return '<User %r>' % self.UserName
