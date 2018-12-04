from flask import Flask, g
from flask_restful import reqparse, Api, Resource
from flask_httpauth import HTTPTokenAuth

# Flask相关变量声明
app = Flask(__name__)
api = Api(app)

# RESTfulAPI的参数解析 -- put / post参数解析
parser_put = reqparse.RequestParser()
parser_put.add_argument("user", type=str, required=True, help="need user data")
parser_put.add_argument("pwd", type=str, required=True, help="need pwd data")


# 功能方法部分案例
def to_do(arg1, args2):
    return {'user': str(arg1), 'pwd': str(args2)}
    # return str(arg1) + str(args2)


# 操作（post / get）资源列表
class TodoList(Resource):

    def post(self):
        args = parser_put.parse_args()

        # 构建新参数
        user = args['user']
        pwd = args['pwd']
        # 调用方法to_do
        info = {"info": to_do(user, pwd)}

        # 资源添加成功，返回201
        return info, 201


# 设置路由，即路由地址为http://127.0.0.1:5000/users
api.add_resource(TodoList, "/users")

if __name__ == "__main__":
    app.run(debug=True)
