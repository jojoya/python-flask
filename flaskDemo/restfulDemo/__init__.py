from restfulDemo.extensions import restful_api
from restfulDemo.controllers.module1.posts import PostApi
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# 创建flask对象
app = Flask(__name__)

# 配置flask配置对象中键
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1/db_jojoya"           # mysql
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True             # 应用会自动在每次请求结束后提交数据库中变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy(app)


def create_app(object_name):
    # Init the Flask-Restful via app object >>  将 restful_api 对象注册到 app 对象中
    # Define the route of restful_api   >>  add_resource() 允许为同一个资源类绑定多条路由
    restful_api.add_resource(
        PostApi,
        '/api/posts',
        '/api/posts/<string:post_id>',      # 表示可以访问 posts 这一类资源中某一个 post_id 一致的资源对象.
        endpoint='restful_api_post')

    # restful_api.add_resource(
    #     PostApi,
    #     '/api/posts')

    restful_api.init_app(app)


