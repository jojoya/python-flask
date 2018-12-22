from flask_restful import Resource, abort, reqparse

USER_LIST = {
    1: {'name':'Michael'},
    2: {'name':'Tom'},
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)


def abort_if_not_exist(user_id):
    if user_id not in USER_LIST:
        abort(404, message="User {} doesn't exist".format(user_id))


class ServiceCheckApi(Resource):
    def get(self):
        return USER_LIST
    def post(self):
        """json传参：{"name":"Jack"}"""
        args = parser.parse_args(strict=True)
        user_id = int(max(USER_LIST.keys())) + 1
        USER_LIST[user_id] = {'name': args['name']}
        return USER_LIST[user_id], 201

class GetRecordData(Resource):
    def get(self, user_id):
        abort_if_not_exist(user_id)
        return USER_LIST[user_id], 201
