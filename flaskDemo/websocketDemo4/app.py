from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS     # 解决跨域请求
from flask_socketio import SocketIO  # 新添加的代码
from config import config
from report.api.views import ServiceCheckApi, GetRecordData
from report.main.views import my_main, socketio

db = SQLAlchemy()
api = Api()

async_mode = None     # 新添加的代码
# socketio = SocketIO()   # 新添加的代码


def app_create(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    app.config['SECRET_KEY'] = 'secret!'    # 临时
    config[config_name].init_app(app)

    db.init_app(app)

    # 路由和其他处理程序定义
    # 注册蓝图
    # from report.main import main as main_blueprint  # 从当前目录下面的main子目录中导入main对象
    # app.register_blueprint(main_blueprint)
    app.register_blueprint(my_main, url_prefix='/my_main')

    api.add_resource(ServiceCheckApi, '/api/service_check')  # api与websocket无关
    api.add_resource(GetRecordData, '/api/get_data/<int:user_id>')
    # add_resource 函数使用指定的endpoint 将路由注册到框架上
    api.init_app(app)  # api初始化必须放在路由注册之后
    CORS(app)  # 跨域请求
    socketio.init_app(app=app, async_mode=async_mode)  # 新添加的代码
    return app
