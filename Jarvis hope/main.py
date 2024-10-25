import json
import os
import re  # Import for text normalization
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
            data = json.load(file)
            print("Debug: Loaded predefined data from file.")  # Debug message
            return data
    print("Debug: No predefined data file found. Starting fresh.")  # Debug message
    return {}

# Save updated predefined data to JSON file
def save_predefined_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)
    print("Debug: Saved predefined data to file.")  # Debug message

# Normalize text by removing punctuation and converting to lowercase
def normalize_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())

def jarvis():
    predefined_data = load_predefined_data()

    while True:
        user_input = input("You: ").strip()
        normalized_input = normalize_text(user_input)

        if normalized_input == "learn":
            predefined_data = jarvis_learn(predefined_data)

        elif normalized_input.startswith("what") or normalized_input.startswith("when") or normalized_input.startswith("who") or normalized_input.startswith("how"):
            question = user_input
            normalized_question = normalize_text(question)
            answer = predefined_data.get(normalized_question)

            if answer:
                print(f"Jarvis: {answer}")  # Confirm answer is from file
            else:
                # Search Wikipedia if not found in predefined data
                try:
                    summary = wikipedia.summary(question, sentences=2)
                    print(f"Jarvis: {summary} (from Wikipedia)")  # Confirm answer is from Wikipedia
                    # Store the question and answer in predefined data
                    predefined_data[normalized_question] = summary
                    save_predefined_data(predefined_data)
                except Exception as e:
                    print("Jarvis: I'm not sure how to handle that request.")

        elif "weather" in normalized_input:
            city = user_input.replace("weather", "").strip()
            result = get_weather(city)
            print(f"Jarvis: {result}")

        elif normalized_input.startswith("play "):
            song_name = user_input[5:]  # Get the song name
            play_youtube_video(song_name)  # Play the song

        elif normalized_input.startswith("schedule "):
            parts = user_input[9:].rsplit(' ', 1)  # Split the command and the time
            if len(parts) == 2:
                task_name, time_str = parts
                schedule_task(task_name, time_str)  # Schedule the task
            else:
                print("Jarvis: Please provide a task and a time in HH:MM format.")

        elif normalized_input.startswith("open "):
            automate(user_input)  # Call the automate function to open applications

        elif normalized_input == "exit":
            print("Jarvis: Goodbye!")
            break

        else:
            print("Jarvis: I'm not sure how to handle that request.")

if __name__ == "__main__":
    jarvis()
