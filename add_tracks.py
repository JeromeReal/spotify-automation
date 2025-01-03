# add_tracks.py
import spotipy
from auth import sp  # Import the authenticated Spotify object

# Fetch top tracks
results = sp.current_user_top_tracks(limit=10)
track_ids = [track['id'] for track in results['items']]

# Add tracks to the playlist
playlist_id = "https://open.spotify.com/playlist/7pcSC2TmyXUTwP9j7TIfQH?si=14c_nF0DTtSvwI_X2RZPHA"  # Replace with your playlist ID
sp.playlist_add_items(playlist_id, track_ids)
print("Tracks added to playlist!")