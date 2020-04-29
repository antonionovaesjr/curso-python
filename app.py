from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/novaes')
def hello_world2():
    return 'Hello2, World2!'