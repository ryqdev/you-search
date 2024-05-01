from flask import jsonify
import json

def pong(request):
    if request.method == 'POST':
        data = json.loads(request.data)
        video_id = data.get('id')
        response = jsonify(video_id)
        return response
    else:
        return '404'