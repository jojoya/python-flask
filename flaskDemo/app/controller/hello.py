from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    # app.env = 'development'
    # app.debug = True
    app.run(host='0.0.0.0', debug=True)