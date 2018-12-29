#!/usr/bin/env python
import json
import logging
import time
from random import choice

from flask import Flask, render_template
from flask_socketio import SocketIO

from utils.tools import randomtime, seconds2time

logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO()
socketio.init_app(app)
@app.route('/')
def index():
    return render_template('index.html')

# 入门
@socketio.on('message')
def handle_msg(message):
    print('received message:　' + str(message))

# 多参数
@socketio.on('my_sustom_event')
def handle_my_sustom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)

# 命名空间
@socketio.on('my_custom_namespace_event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('my_custom_namespace_event received json: ' + str(json))
    socketio.emit('my_custom_namespace_event received json: ' + str(json))
    return json
# 有时，装饰器的语法并不方便，on_event()方法可以作为替代
# socketio.on_event('my_custom_namespace_event', handle_my_custom_namespace_event, namespace='/test')

# 信息回调，返回给客户端
@socketio.on('return_message')
def handle_return_message(message):
    return_message = 'return_message received message: ' + str(message)
    print(return_message)
    # return(return_message, 2)
    return return_message

@socketio.on('svr_send_json')
def handle_svr_send_json(json):
    print('svr_send_json received json: ' + str(json))
    send(json, json=True)

# 发送消息
from flask_socketio import send, emit
# @socketio.on('svr_send_message', namespace='/test')
def handle_svr_send_message(message):
    print('svr_send_message received message: ' + str(message))
    # socketio.emit('server_response', message, namespace='/test')
    times = randomtime()
    for r in times:
        case = ['1', '2', '3', '4', '5']
        step = ['1', '2', '3', '4', '5']
        msg = [(200, '成功'), (201, '失败')]
        msg_info = choice(msg)

        ws_result = Ws_exec_result()
        ws_result.exec_time = seconds2time(r)
        ws_result.case_id = choice(case)
        ws_result.step_id = choice(step)
        ws_result.code = msg_info[0]
        ws_result.msg = msg_info[1]

        data_dict = ws_result.__dict__
        # data_json = json.dumps(data_dict)

        data = {'data': data_dict}
        print(data)
        emit('server_response', data)
        time.sleep(1)


# @socketio.on('client_msg', namespace='/test')
def client_msg(msg):
    print('client_msg: ' + str(msg))
    socketio.emit('server_msg', msg, namespace='/test')

class Ws_exec_result:
    def __init__(self, code=200, msg=None, case_id=None, step_id=None, request_header=None, request_cookie=None, request_data=None, response_header=None, response_cookie=None, response_data=None, exec_time=None):
        self.code = code
        self.msg = msg
        self.case_id = case_id
        self.step_id = step_id
        self.request_header = request_header
        self.request_cookie = request_cookie
        self.request_data = request_data
        self.response_header = response_header
        self.response_cookie = response_cookie
        self.response_data = response_data
        self.exec_time = exec_time


if __name__ == '__main__':
    socketio.on_event('client_msg', client_msg, namespace='/test')
    socketio.on_event('svr_send_message', handle_svr_send_message, namespace='/test')

    app.run(host='0.0.0.0', port=5001, debug=True)
    # socketio.run(app, host='0.0.0.0', port=5001, debug=True)