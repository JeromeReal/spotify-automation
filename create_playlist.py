# create_playlist.py
import spotipy
from auth import sp  # Import the authenticated Spotify object

# Create a new playlist
user_id = sp.me()['id']
playlist = sp.user_playlist_create(user_id, "My Python Playlist", public=True)
print(f"Playlist created: {playlist['name']}")