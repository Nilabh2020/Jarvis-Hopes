import json
import os
from weather_info import get_weather
from jarvis_learn import jarvis_learn
from automation import automate
from scheduler import schedule_task
from YTvid import play_youtube_video
import wikipedia
from send_email import send_email


# File path for the predefined data
DATA_FILE = 'predefined_data.json'

# Load predefined data from JSON file
def load_predefined_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save predefined data to JSON file
def save_predefined_data(predefined_data):
    with open(DATA_FILE, 'w') as file:
        json.dump(predefined_data, file, indent=4)

# Send an email

def jarvis():
    predefined_data = load_predefined_data()

    while True:
        user_input = input("You: ").lower().strip()
        print(f"Debug: User input received: '{user_input}'")  # Debug statement

        if user_input == "learn":
            predefined_data = jarvis_learn(predefined_data)

        elif user_input.startswith("what") or user_input.startswith("when") or user_input.startswith("who"):
            question = user_input
            answer = predefined_data.get(question)

            if answer:
                print(f"Jarvis: {answer}")
            else:
                try:
                    summary = wikipedia.summary(question, sentences=2)
                    print(f"Jarvis: {summary}")
                    predefined_data[question] = summary
                    save_predefined_data(predefined_data)
                except Exception as e:
                    print("Jarvis: I'm not sure how to handle that request.")

        elif "weather" in user_input:
            city = user_input.replace("weather", "").strip()
            result = get_weather(city)
            print(f"Jarvis: {result}")

        elif user_input.startswith("play "):
            song_name = user_input[5:]  # Get the song name
            play_youtube_video(song_name)

        elif user_input.startswith("schedule "):
            parts = user_input[9:].rsplit(' ', 1)
            if len(parts) == 2:
                task_name, time_str = parts
                schedule_task(task_name, time_str)
            else:
                print("Jarvis: Please provide a task and a time in HH:MM format.")

        elif user_input.startswith("open "):
            automate(user_input)

        elif user_input == "email":  # Ensure this is checking for 'email'
            print("Debug: Calling send_email() function...")  # Debug statement
            send_email()  # Call the email function when 'email' is typed

        elif user_input == "exit":
            print("Jarvis: Goodbye!")
            break

        else:
            print("Jarvis: I'm not sure how to handle that request.")

if __name__ == "__main__":
    jarvis()
