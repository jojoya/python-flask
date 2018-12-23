import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


"""
对app进行一些路由设置
"""


@app.route('/')
def index():
    return render_template('index.html')


"""
对socketio进行一些监听设置
"""


@socketio.on('request_for_response',namespace='/test')
def give_response(data):
    value = data.get('param')
    print(value)
    # 进行一些对value的处理或者其他操作,在此期间可以随时会调用emit方法向前台发送消息
    emit('response', {'code': '200', 'msg': 'start to process...'})
    time.sleep(5)
    emit('response', {'code': '200', 'msg': 'processed'})


@socketio.on('my event', namespace='/test')
def test_message(message):
    print("my event")
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    print("my broadcast event")
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/test')
def test_connect():
    print("connect")
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    # 这里就不再用app.run而用socketio.run了。socketio.run的参数和app.run也都差不多
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
