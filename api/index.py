from flask import Flask, request
from flask_cors import CORS
import utils.youtube as yt

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/tldr', methods=['POST'])
def tldr():
    return yt.tldr(request)
