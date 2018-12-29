#coding=utf8
from socketIO_client import SocketIO, BaseNamespace


class TestNamespace(BaseNamespace):
    def on_aaa_response(self, *args):
        print('on_aaa_response', args)
#
#
# socketIO = SocketIO('localhost', 5000)
# chat_namespace = socketIO.define(TestNamespace, '/test')
#
# chat_namespace.emit("{data: 'message!'}")
# socketIO.wait(seconds=1)


# def on_bbb_response(*args):
#     print('on_bbb_response', args)
#
# with SocketIO('localhost', 5000, TestNamespace) as socketIO:
#     socketIO.emit('server_response', {'data': 'yyy'}, on_bbb_response)
#     socketIO.wait_for_callbacks(seconds=1)


def on_response(*args):
    print('on_response', args)

socket = SocketIO('localhost',5000)
chat = socket.define(BaseNamespace, '/test')
# chat.emit('message')
chat.emit('server_response', {'data': 'yyy'}, on_response)
# chat.on('my response', on_response)