from socketIO_client import SocketIO, BaseNamespace


class TestNamespace(BaseNamespace):
    def on_connect(self):
        print('[Connected]')

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')

    def on_aaa_response(self, *args):
        print('on_aaa_response', args)

def on_client_event_response(*args):
        print('收到message消息:', args)
        print('type:', type(args))
        if len(args) > 0:
            print('收到message消息', str(args[0], encoding='utf-8'))


socketIO = SocketIO(host='localhost', port=5001, Namespace=TestNamespace)
test_namespace = socketIO.define(TestNamespace, '/test')

test_namespace.emit('connect_event', {'data': '消息'}, callback=on_client_event_response)
socketIO.wait_for_callbacks(seconds=1)

# data_msg = {'data': '消息'}
# data = {"sn": 0, "ver": 2}
# data_connect = {'data': '连接'}
# i = 0
# while i < 5:
#     test_namespace.emit('client_event', data_msg, callback=on_client_event_response)
#     socketIO.wait_for_callbacks(seconds=1)
#     i = i + 1

# socketIO.wait(seconds=1)