import json
import logging
logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)


from socketIO_client import SocketIO

hosts = 'http://localhost'
port = 5001


# 收到message消息处理过程
def on_message(*args):
    print('收到message消息:', args)
    print('type:', type(args))
    if len(args) > 0:
        print('收到message消息', str(args[0], encoding='utf-8'))

def on_client_event_response(*args):
    print('收到message消息:', args)
    print('type:', type(args))
    if len(args) > 0:
        print('收到message消息', str(args[0], encoding='utf-8'))


sk = SocketIO(hosts, port=port)
# sk = SocketIO(hosts, port=port, params={'data': 'ksdjfkjdf'})  # create connection with params

# add lisenter for message response
sk.on('message', on_message)
# sk.on('message', on_message, path='/test')

data = {"sn": 0, "ver": 2}
data_connect = {'data': '连接'}
data_msg = {'data': '消息'}
# send data to message
# sk.emit('connect_event1', data, on_message)
sk.emit('client_event', data_msg, on_client_event_response, path='/test')
# sk.emit('message', data_msg, on_message, path='/test')
# send data to login
# sk.send(data, on_message)  # default send data to message

sk.wait_for_callbacks(seconds=1)
