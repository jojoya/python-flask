from websocket import create_connection

ws_server = "ws://192.168.1.221:8000/websocket/"
ws = create_connection(ws_server)
ws.send('hello,python')  # 发送数据
print(ws.recv())  # 获取数据
ws.send('欢迎光临我的博客')
print(ws.recv())

ws.close()