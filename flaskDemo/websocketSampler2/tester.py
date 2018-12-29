import json
import logging

from flask_socketio import emit, send

logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)


from socketIO_client import SocketIO, BaseNamespace

hosts = 'http://localhost'
port = 5001


# 收到message消息处理过程
def on_message(*args):
    print('收到message消息:', args)
    print('type:', type(args))
    if len(args) > 0:
        print('我发送到服务端的message是： ', str(args[0]))

socketIO = SocketIO(hosts, port=port)
# 入门
# socketIO.emit('message', {'data': 'message消息'}, callback=on_message)
# socketIO.send({'data': 'message消息'}, callback=on_message)
# 多参数
# arg1 = arg2 = arg3 = ' 123abc '
# socketIO.emit('my_sustom_event', arg1, arg2, arg3, callback=on_message)
# 命名空间
# class TestNamespace(BaseNamespace):
#     def on_connect(self):
#         print('[Connected]')
#     def on_reconnect(self):
#         print('[Reconnected]')
#     def on_disconnect(self):
#         print('[Disconnected]')
#     def on_my_custom_namespace_event_response(self, *args):
#         print('on_my_custom_namespace_event_response', args)
# test_namespace = socketIO.define(TestNamespace, '/test')
# test_namespace.emit('my_custom_namespace_event', ' 123abc ', callback=on_message)
# 服务端返回信息
# socketIO.emit('return_message', ' 123abc ', callback=on_message)
# 发送消息
socketIO.emit('svr_send_message', ' 123abc ', callback=on_message)
socketIO.wait_for_callbacks(seconds=1)
