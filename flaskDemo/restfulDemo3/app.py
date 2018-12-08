from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import config

# 创建flask对象
app = Flask(__name__)

# 配置flask配置对象中键
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@10.0.108.220:3306/apitest?charset=utf8"
app.config.from_object(config["development"])
api = Api(app)

# 获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy()
db.init_app(app)



