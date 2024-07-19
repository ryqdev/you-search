from flask import Flask, request
from flask_cors import CORS
import utils.youtube as yt
from utils.handle_post import pong

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/ping', methods=['POST'])
def ping():
    return pong(request)

@app.route('/tldr', methods=['POST'])
def tldr():
    return yt.tldr(request)

# Test of ping

"""
curl --request POST \
  --url https://you-search-zeta.vercel.app/ping \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.3.2' \
  --data '{
	"id": 123
}'
"""