from demo1.my_app import db


# 创建模型对象
class User(db.Model):
    __tablename__ = 't_user'

    # id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, username, email, id=None):
        self.username = username
        self.email = email
        if id != None:
            self.id = id

    def __str__(self):
        return User.__str__()

    def __repr__(self):
        return '<User %r>' % self.username


# 1.创建表
db.create_all()
