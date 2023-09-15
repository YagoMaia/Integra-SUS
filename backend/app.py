from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/user/<user_id>/')
def user(user_id):
    return f'Hello World, user number {user_id}'