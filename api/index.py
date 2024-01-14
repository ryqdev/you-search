from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json
from youtube_transcript_api import YouTubeTranscriptApi

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
    if request.method == 'POST':
        data = json.loads(request.data)
        video_id = data.get('video_id') # Retrieve the video_id from the JSON payload
        subtitles = get_subtitles(video_id)
        # Convert subtitles to a JSON response

        response = jsonify(subtitles)
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response

def get_subtitles(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    for transcript in transcript_list:
        result = transcript.fetch()
        if result is not None:
            return result

    return ""
