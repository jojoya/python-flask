#!/usr/bin/env python
import time

from flask import Flask, render_template
from flask_socketio import Namespace, emit, SocketIO

from utils.tools import get_date_time
import logging

logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('client_event', namespace='/test')
def client_msg(msg):
    print("客户端发送msg消息>>>", msg)
    info = get_date_time() + ': ' + msg['data']
    print(info)
    # emit('server_response', {'data': info})
    # emit('server_response', "{'data': info}")
    socketio.send('server_response', {'data': info}, '/test', callback='on_client_event_response')
    # i = 0
    # while i < 5:
    #     info = get_date_time() + ': ' + msg['data']
    #     print(info)
    #     emit('server_response', {'data': info})
    #     i = i + 1
    #     time.sleep(1)

@socketio.on('message', namespace='/test')
def client_json(json):
    print("客户端发送json消息>>>", json)
    # info = get_date_time() + ': ' + json['data']
    emit('server_response', {'data': json['data']})


@socketio.on('connect_event', namespace='/test')
def connected_msg(msg):
    print("客户端发起连接>>>", msg)
    i = 0
    while i < 5:
        info = get_date_time() + ': ' + msg['data']
        emit('server_response', {'data': info})
        i = i + 1
        time.sleep(1)


@socketio.on('connect_event1')
def connected_msg1(msg):
    print("客户端发起连接connect_event1>>>", msg)
    # info = get_date_time() + ', ' + msg
    emit('server_connect_response', {'data': msg})

@socketio.on('client_event1')
def client_msg1(msg):
    print("客户端发送msg消息client_event1>>>", msg)
    # info = get_date_time() + ', ' + str(msg)
    emit('server_msg_response', {'data': msg})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)