from flask import Blueprint, url_for
from flask_restful import Resource, reqparse, abort, fields, marshal, marshal_with
from flask_sqlalchemy import BaseQuery

from restfulDemo3.Case import Case
from restfulDemo3.app import api, app

case_manager = Blueprint("case", __name__)


def make_public_case(case):
    new_case = {}
    for field in case:
        if field == 'id':
            new_case['uri'] = url_for('get_case', task_id=case['id'], _external=True)
        else:
            new_case[field] = case[field]
    return new_case


case_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'desc': fields.Boolean
}

cases = [
    {
        'id': 1,
        'name': u'Buy groceries',
        'desc': u'Milk, Cheese, Pizza, Fruit, Tylenol'
    },
    {
        'id': 2,
        'name': u'Learn Python',
        'desc': u'Need to find a good Python tutorial on the web'
    }
]


class CaseAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='用例id不能为空', location='json')
        self.reqparse.add_argument('name', type=str, default="", location='json')
        self.reqparse.add_argument('desc', type=str, default="", location='json')
        super(CaseAPI, self).__init__()

    @marshal_with(case_fields)
    def get(self, id):
        # case = filter(lambda t: t['id'] == id, cases)
        # if len(case) == 0:
        #     abort(404)
        # return {'task': case[0]}
        case = Case.query.get(id)
        if case:
            case = case.__dict__
            case.pop('_sa_instance_state', None)
            print(case)
        return case

    def put(self, id):
        # cases = Case.query.all()
        case = filter(lambda t: t['id'] == id, cases)
        if len(case) == 0:
            abort(404)
        case = case[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                case[k] = v
        return {'task': marshal(case, case_fields)}
        # return {'case': make_public_task(case)},201   # Flask-RESTful 会自动地处理转换成 JSON 数据格式

    def delete(self, id):
        pass


class CaseListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='用例标题不能为空', location='json')
        self.reqparse.add_argument('desc', type=str, default="", location='json')
        super(CaseListAPI, self).__init__()

    def get_all(self):
        with app.app_context():
            query: BaseQuery = Case.query
            cases = query.all()
            # cases = Case.query.all()
            print(cases)
            case = cases[0].__dict__
            case.pop('_sa_instance_state', None)
            print(case)
        return case

    def get(self):
        with app.app_context():
            query: BaseQuery = Case.query
            cases = query.all()
            # cases = Case.query.all()
            print(cases)
            case = cases[0].__dict__
            case.pop('_sa_instance_state', None)
            print(case)
        return case

    def post(self):
        pass


api.add_resource(CaseListAPI, '/cases', endpoint='users')
api.add_resource(CaseAPI, '/cases/<int:id>', endpoint='user')

if __name__ == '__main__':
    app.run(debug=True)
