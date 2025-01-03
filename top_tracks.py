# top_tracks.py
import spotipy
from auth import sp  # Import the authenticated Spotify object

# Fetch top tracks
results = sp.current_user_top_tracks(limit=10)

# Print the top tracks
print("Your Top 10 Tracks:")
for idx, item in enumerate(results['items']):
    print(f"{idx+1}: {item['name']} by {', '.join(artist['name'] for artist in item['artists'])}")