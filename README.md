# Spotify Automation Project

This project demonstrates how to interact with the Spotify Web API using Python. It is designed as a portfolio project to showcase the ability to authenticate with Spotify, fetch user data, and automate tasks like creating playlists, fetching top tracks, and searching for songs.

## Features
- Authenticate with Spotify using OAuth 2.0.
- Fetch the user's top tracks.
- Create and manage playlists.
- Search for tracks in the Spotify catalog.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- A Spotify Developer Account ([Sign up here](https://developer.spotify.com/dashboard/))

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JeromeReal/spotify-automation
   cd spotify-automation
   ```

2. **Set Up Spotify Developer App**:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new app and obtain your **Client ID** and **Client Secret**.
   - Add the following redirect URI in your app settings: `http://localhost:8888/callback`.

3. **Run the Authentication Script**:
   - Execute the script and input your **Client ID** and **Client Secret** when prompted:
     ```bash
     python auth.py
     ```

4. **Run Other Scripts**:
   - Fetch top tracks:
     ```bash
     python top_tracks.py
     ```
   - Create a playlist:
     ```bash
     python create_playlist.py
     ```
   - Add tracks to a playlist:
     ```bash
     python add_tracks.py
     ```
   - Search for tracks:
     ```bash
     python search_tracks.py
     ```

## Folder Structure
```
spotify-automation/
│
├── auth.py                # Authentication script
├── top_tracks.py          # Script to fetch user's top tracks
├── create_playlist.py     # Script to create a new playlist
├── add_tracks.py          # Script to add tracks to a playlist
├── search_tracks.py       # Script to search for tracks
└── README.md              # Project documentation
```

## Important Notes
- This project is for portfolio purposes only. Ensure your **Client ID** and **Client Secret** are kept secure and not shared publicly.
- If you plan to share this repository publicly, avoid hardcoding sensitive information in the scripts.

## License
This project is licensed under the MIT License.

