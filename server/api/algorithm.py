from .song import Song
#from movie import Mo
from decouple import config
import requests
import base64
import datetime

class Algorithm:

    spotify_token = None
    spotify_token_expiration = datetime.datetime.min
    spotify_token_url = "https://accounts.spotify.com/api/token"
    spotify_api_url = "https://api.spotify.com/v1/"
    SPOTIFY_CLIENT_ID = config("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET")
    
    songs = []
    movies = [] 

    @classmethod
    def get_spotify_token(cls) -> str:
        if cls.spotify_token is None or datetime.datetime.now() >= cls.spotify_token_expiration:
            headers = {
                "Authorization": "Basic " + base64.b64encode((cls.SPOTIFY_CLIENT_ID + ":" + cls.SPOTIFY_CLIENT_SECRET).encode()).decode(),
                "Content-Type": "application/x-www-form-urlencoded"
            }
            payload = {"grant_type": "client_credentials"}
            request = requests.post(cls.spotify_token_url, data=payload, headers=headers)
            response = request.json()
            cls.spotify_token = response["access_token"]
            cls.spotify_token_expiration = datetime.datetime.now() + datetime.timedelta(seconds=response["expires_in"])
            return cls.spotify_token
        else:
            return cls.spotify_token