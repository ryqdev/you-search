from flask import Flask, request
import json
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/tldr', methods = ['POST', 'GET'])
def tldr():
    if request.method == 'GET':
        return "tldr"
    else:
        json_str = request.body.decode('utf-8')
        json_data = json.loads(json_str)
        video_id = json_data['video_id']
        subtitles = json.dumps(get_subtitles(video_id))
        return subtitles 

def get_subtitles(video_id):
    # video_id = extract_video_id(url)

    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    # iterate over all available transcripts
    for transcript in transcript_list:
        result = transcript.fetch()
        if result is not None:
            return result

    return ""
