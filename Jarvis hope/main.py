import json
import os
from dotenv import load_dotenv
from weather_info import get_weather
from jarvis_learn import jarvis_learn
from automation import automate  # Import the automate function
from scheduler import schedule_task  # Import the schedule_task function
from YTvid import play_youtube_video  # Import the play_youtube_video function
import wikipedia  # Ensure you have this import for Wikipedia functionality

# Load environment variables from .env file
load_dotenv()

# File path for the predefined data
DATA_FILE = 'predefined_data.json'

# Load predefined data from JSON file
def load_predefined_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def jarvis():
    predefined_data = load_predefined_data()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "learn":
            predefined_data = jarvis_learn(predefined_data)

        elif user_input.startswith("what") or user_input.startswith("when") or user_input.startswith("who"):
            question = user_input
            answer = predefined_data.get(question)

            if answer:
                print(f"Jarvis: {answer}")
            else:
                # Search Wikipedia if not found in predefined data
                try:
                    summary = wikipedia.summary(question, sentences=2)
                    print(f"Jarvis: {summary}")
                except Exception as e:
                    print("Jarvis: I'm not sure how to handle that request.")

        elif "weather" in user_input:
            city = user_input.replace("weather", "").strip()
            result = get_weather(city)
            print(f"Jarvis: {result}")

        elif user_input.startswith("play "):
            song_name = user_input[5:]  # Get the song name
            play_youtube_video(song_name)  # Play the song

        elif user_input.startswith("schedule "):
            parts = user_input[9:].rsplit(' ', 1)  # Split the command and the time
            if len(parts) == 2:
                task_name, time_str = parts
                schedule_task(task_name, time_str)  # Schedule the task
            else:
                print("Jarvis: Please provide a task and a time in HH:MM format.")

        elif user_input.startswith("open "):
            automate(user_input)  # Call the automate function to open applications

        elif user_input == "exit":
            print("Jarvis: Goodbye!")
            break

        else:
            print("Jarvis: I'm not sure how to handle that request.")

if __name__ == "__main__":
    jarvis()
