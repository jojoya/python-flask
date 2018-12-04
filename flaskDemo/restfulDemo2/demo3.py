#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    1: {'task': 'build an API'},
    2: {'task': '哈哈哈'},
    3: {'task': 'profit!'},
}
current_max_todo_id = max(TODOS)  # assert isinstance(current_max_todo_id, int)

parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, todo_id):
        global TODOS
        if todo_id not in TODOS:
            abort(404, message="todo item {} doesn't exist".format(todo_id))
        return TODOS[todo_id]

    def delete(self, todo_id):
        global TODOS
        if todo_id not in TODOS:
            abort(404, message="todo item {} doesn't exist".format(todo_id))
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        global TODOS
        global parser
        global current_max_todo_id
        args = parser.parse_args()
        current_max_todo_id = max(todo_id, current_max_todo_id)
        task = {current_max_todo_id: args.get('task', '')}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        global TODOS
        return TODOS

    def post(self):
        global TODOS
        global parser
        args = parser.parse_args()
        todo_id = self.get_next_todo_id()
        TODOS[todo_id] = {'task': args.get('task', '')}
        return TODOS[todo_id], 201

    def get_next_todo_id(self):
        global current_max_todo_id
        current_max_todo_id += 1
        return current_max_todo_id


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
