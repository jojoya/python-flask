from flask import Flask

from demoSampler.src.myviews import login, first_flask

app = Flask(__name__, template_folder='src/templates')

# 如果app实例和views分开，需要用这种方式启动
app.add_url_rule("/login", "login", login, methods=['GET'])
app.add_url_rule("/", "first_flask", first_flask, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)