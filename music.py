import os
import yt_dlp

# Create 'music' folder if it doesn't exist
output_folder = "music"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get playlist URL from user
playlist_url = input("Enter YouTube Playlist URL: ")

# yt-dlp download options
ydl_opts = {
    'format': 'bestaudio/best',
    'ignoreerrors': True,
    'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': False,
    'quiet': False,
    # correct extractor args format for Python API
    'extractor_args': {
        'youtube': {
            'player_client': ['android']
        }
    }
}

# Start download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
