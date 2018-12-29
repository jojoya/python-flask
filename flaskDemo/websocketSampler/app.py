#!/usr/bin/env python
import time
from time import sleep

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

from utils.tools import get_date_time

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('client_event', namespace='/test')
def client_msg(msg):
    print("客户端发送msg消息>>>", msg)
    # info = get_date_time() + ', ' + msg['data']
    info = get_date_time() + ', ' + str(msg)
    emit('server_response', {'data': info})


@socketio.on('client_event_json', namespace='/test')
def client_json(json):
    print("客户端发送json消息>>>", json)
    info = get_date_time() + ', ' + json['data']
    emit('server_response', {'data': info})


@socketio.on('connect_event', namespace='/test')
def connected_msg(msg):
    print("客户端发起连接>>>", msg)
    info = get_date_time() + ', ' + msg['data']
    emit('server_response', {'data': info})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)