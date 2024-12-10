import webbrowser

def play_latest_song(artist):
    search_query = f"{artist} latest song"
    youtube_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
    webbrowser.open(youtube_url)
    print(f"Jarvis: Searching YouTube for the latest song by {artist}...")
