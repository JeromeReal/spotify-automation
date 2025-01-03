import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = input("Enter your Spotify Client ID: ")
CLIENT_SECRET = input("Enter your Spotify Client Secret: ")
REDIRECT_URI = "http://localhost:8888/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read user-top-read playlist-modify-public"
))
