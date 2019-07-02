from flask import Flask
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(1)

app = Flask(__name__)


@app.route('/synchronize')
def update_redis():
    executor.submit(do_update)
    print('ok')
    return 'ok'


def do_update():
    time.sleep(3)
    print('start update')

def update_info(info):
    executor.submit(update_do)
    print(info)
    return 'ok'

def update_do():
    time.sleep(1)
    print('start update_do')


if __name__ == '__main__':
    # app.run()
    i = 0
    while i < 5:
        # update_redis()
        update_info(str(i))
        i = i + 1
    # executor.submit(update_info('1'))
    # executor.submit(update_info('2'))
    # executor.submit(update_info('3'))
    # executor.submit(update_info('4'))
    # executor.submit(update_info('5'))
    # executor.submit(update_info('6'))

