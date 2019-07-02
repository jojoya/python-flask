
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# test 是链接的数据库
app.config['MONGODB_SETTINGS'] = {
    'db': 'jojoya_DB',
    'host': '10.0.109.91',
    'port': 27017
}
# 实例化
# db = MongoEngine(app)
# 创建mongo原型
mdb = MongoEngine()
mdb.init_app(app)


if __name__ == '__main__':
    app.run()