# search_tracks.py
import spotipy
from auth import sp  # Import the authenticated Spotify object

# Search for tracks
query = "Imagine Dragons"
search_results = sp.search(q=query, limit=5, type='track')

print(f"Search results for '{query}':")
for idx, item in enumerate(search_results['tracks']['items']):
    print(f"{idx+1}: {item['name']} by {', '.join(artist['name'] for artist in item['artists'])}")
