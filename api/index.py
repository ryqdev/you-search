from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About123'

@app.route('/tldr')
def tldr():
    return 'tldr'