import openai
import requests
import os
openai.api_key = os.environ['KEY_API']

SENT = f"""raiva, alegria, medo, nojo, tristeza, satisfação, confiança, amor"""

def get_music_lyric(artist_name, track_name):
    url = f'http://api.musixmatch.com/ws/1.1/matcher.lyrics.get'
    params = {
        'format': 'json',
        'q_artist': artist_name,
        'q_track': track_name,
        'apikey': os.environ['MUSIX']
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and data['message']['header']['status_code'] == 200:
        lyrics = data['message']['body']['lyrics']['lyrics_body']
        lyrics = lyrics.replace("\n******* This Lyrics is NOT for Commercial use *******\n(1409623849948)", "") if type(lyrics) == str and "\n******* This Lyrics is NOT for Commercial use *******\n(1409623849948)" in lyrics else lyrics
        return lyrics
    
    return None

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_sentiment_by_lyrics(music):

    prompt = f"""
    De acordo com a lista com os sentimentos {SENT} \
    Me retorne um html indicando um sentimento dessa lista para cada trecho da música abaixo. \
    O html terá apenas tags <p>. Cada trecho vai ser uma tag <p> e o id da tag será o sentimento. \

    {music} \
    """

    response = get_completion(prompt)
    return {"html": response}

def get_sentiment_by_title(artist, track):
    lyric = get_music_lyric(artist, track)
    if not lyric:
        raise Exception("None lyric")
    else:
        response = get_sentiment_by_lyrics(lyric)
        return response