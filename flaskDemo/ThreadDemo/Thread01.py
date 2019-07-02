# Flask
import socket
import sys
import time
# from asyncio import Queue
import multiprocessing
from importlib import reload

from flask import Flask, request, g
import os

from flask_socketio import SocketIO

reload(sys)
# sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config.update(DEBUG=True)

socketio = SocketIO(app)
# 获取本机电脑名
myname = socket.getfqdn(socket.gethostname())

# 获取本机ip
myaddr = socket.gethostbyname(myname)
myport = 8912

# msg_queue = Queue(maxsize=5000)
msg_queue = multiprocessing.Queue(5000)


@app.route('/test1')
def the_test1():
    print("test1 print start")
    time.sleep(10)
    print("test1 print after sleep")
    msg = read_queue(msg_queue)

    return 'test1 asyn > ' + str(msg)


@app.route('/test2')
def the_test2():
    print("test2 print!")
    msg = read_queue(msg_queue)
    return 'test2 return > ' + str(msg)


def write_queue(queue):
    # 循环写入数据
    for i in range(10):
        if queue.full():
            print("队列已满!")
            break
        # 向队列中放入消息
        queue.put(i)
        print(i)
        time.sleep(0.5)


def read_queue(queue):
    # 循环读取队列消息
    # while True:
        # 队列为空，停止读取
        if queue.empty():
            print("---队列已空---")
            return "---队列已空---"
            # break

        # 读取消息并输出
        result = queue.get()
        print(result)
        return result


if __name__ == '__main__':
    # socketio.run()
    p1 = multiprocessing.Process(target=write_queue, args=(msg_queue,))
    p1.start()

    # while True:
    #     print(msg_queue.get_nowait())

    app.run(host=myaddr, port=myport, debug=False, threaded=True)  ### threaded开启以后 不需要等队列 threaded=True
    # 或者
    # app.run(host=myaddr,port=myport,debug=False,processes=3) ### processes=N 进程数量，默认为1个
