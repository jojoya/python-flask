# from socketIO_client import SocketIO
# import logging
import socketio

# standard Python
sio = socketio.Client()

# asyncio
# sio = socketio.AsyncClient()

sio.connect('http://localhost:5000', namespaces=['/test'])

sio.emit('client_event', {'foo': 'bar'}, namespace='/test')

sio.disconnect()













# logging.getLogger('requests').setLevel(logging.WARNING)
# logging.basicConfig(level=logging.DEBUG)
#
# hosts = 'http://127.0.0.1'
# port = 5000
#
#
# # 收到message消息处理过程
# def on_message(*args):
#     # print "recv:", args
#     # print "geted:", type(args[0])
#     if type(args[0]):
#         rp = args[0]
#         print("recv:", rp)
#
#
# sk = SocketIO(hosts, port=port)
# sk = SocketIO(hosts, port=port, params={'token': 'ksdjfkjdf'})  # create connection with params
#
# # add lisenter for message response
# sk.on('message', on_message)
#
# data = {
#     "sn": 0,
#     "ver": 2}
# # send data to message
# sk.emit('message', data, on_message)
# sk.send(data, on_message)  # default send data to message
# # send data to login
# sk.emit('login', data, on_message)
#
# sk.wait_for_callbacks(seconds=1)


