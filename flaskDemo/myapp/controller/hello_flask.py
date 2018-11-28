from flask import Flask, request, render_template, jsonify
from flask import current_app

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/info')
def info():
    data = {'id':123456,'name':'jojoya','message':'Welcome to python world!'}
    # return json.dumps(data)
    return jsonify(data)


def valid_login(username, password):
    current_app.logger.debug('current_app.logger value for debugging')
    current_app.logger.warning('current_app.logger warning occurred (%d apples)', 42)
    current_app.logger.error('current_app.logger error occurred')
    if username == "jojoya" and password == "123456":
        return True
    else:
        return False


def log_the_user_in(username):
    app.logger.debug('myapp.logger value for debugging')
    app.logger.warning('myapp.logger warning occurred (%d apples)', 42)
    app.logger.error('myapp.logger error occurred')    # 按照用户名查找用户信息
    # data = {'id': 123456, 'name': username, 'message': 'You have requested by POST method.'}
    data = dict(id="1", name=username, message="You have requested by POST method.")
    return jsonify(data)    # 返回json数据用jsonify


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


if __name__ == "__main__":
    # myapp.env = 'development'
    # myapp.debug = True
    app.run(host='0.0.0.0', debug=True)

