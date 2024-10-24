import webbrowser
import urllib.parse

def play_youtube_video(song_name):
    search_query = urllib.parse.quote(song_name)
    youtube_url = f"https://www.youtube.com/results?search_query={search_query}"

    # Open the search results in the default browser
    print(f"Jarvis: Here are the search results for '{song_name}'.")
    webbrowser.open(youtube_url)

# Example usage (can be removed when integrated into main.py)
if __name__ == "__main__":
    song_name = input("Enter a song name to play: ")
    play_youtube_video(song_name)
