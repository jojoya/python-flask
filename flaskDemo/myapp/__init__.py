# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    print("config:")
    print(config)
    app = Flask(__name__)

    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    my_config = config[config_name]
    app.config.from_object(my_config)
    my_config.init_app(app)

    db.init_app(app)
    db.app = app

    # 注册蓝本
    # 增加auth蓝本
    from myapp.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 附加路由和自定义的错误页面

    return app
