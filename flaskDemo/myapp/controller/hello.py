from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    # myapp.env = 'development'
    # myapp.debug = True
    app.run(host='0.0.0.0', debug=True)