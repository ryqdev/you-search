from youtube_transcript_api import YouTubeTranscriptApi
from flask import jsonify
import json


def tldr(request):
    if request.method == 'POST':
        data = json.loads(request.data)
        video_id = data.get('video_id')
        subtitles = get_subtitles(video_id)
        response = jsonify(subtitles)
        return response
    else:
        return '404'


def get_subtitles(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    for transcript in transcript_list:
        result = transcript.fetch()
        if result is not None:
            return result

    return ""
