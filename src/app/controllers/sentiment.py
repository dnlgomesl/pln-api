from flask_api import status as flask_status
from app.util import make_response, make_error
from app.services import sentiment as service

def get_sentiment(request):
    try:
        body = request.get_json()
        if "lyrics" in body:
            music = str(body["lyrics"])
            sentiment_response = service.get_sentiment_by_lyrics(music)
            return make_response(sentiment_response, flask_status.HTTP_201_CREATED)
        elif "artist" in body and "track" in body:
            artist = str(body["artist"])
            track = str(body["track"])
            sentiment_response = service.get_sentiment_by_title(artist, track)
            return make_response(sentiment_response, flask_status.HTTP_201_CREATED)
        else:
            return make_error(f'Something wrong happened: No valid body.', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)