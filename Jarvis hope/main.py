import json
import os
from dotenv import load_dotenv
from weather_info import get_weather  # Now using the updated weather function
from jarvis_learn import jarvis_learn
from automation import automate
from YTvid import play_youtube_video
from llm_handler import get_assistant_reply
from play_song import play_latest_song  # Play latest song functionality
from cpu_status import get_cpu_usage  # CPU usage status
import threading  # For parallel execution of speak_text
from website_search import open_website_with_search  # Import the search function
from google_calender import list_events, add_event  # Google Calendar Integration
from voice_output import speak_text  # Import the speak_text function

import asyncio  # Import asyncio to run async functions

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

# Make the jarvis function async
async def jarvis():
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
                # Speak in a separate thread
                threading.Thread(target=lambda: asyncio.run(speak_text(answer))).start()
            else:
                try:
                    llm_response = get_assistant_reply(user_input)
                    print(f"Jarvis: {llm_response}")
                    # Speak in a separate thread
                    threading.Thread(target=lambda: asyncio.run(speak_text(llm_response))).start()
                except Exception as e:
                    print(f"Jarvis: Sorry, I couldn't process your request. Error: {e}")
                    # Speak in a separate thread
                    threading.Thread(target=lambda: asyncio.run(speak_text("Sorry, I couldn't process your request."))).start()

        elif "weather" in user_input:
            city = user_input.replace("can you tell the weather of", "").strip()
            result = get_weather(city)  # Use the scraping function to get weather data
            print(f"Jarvis: {result}")
            # Speak in a separate thread
            threading.Thread(target=lambda: asyncio.run(speak_text(result))).start()

        elif user_input.startswith("play the latest song by"):
            artist = user_input.replace("play the latest song by", "").strip()
            play_latest_song(artist)

        elif user_input.startswith("play "):
            song_name = user_input[5:]  # Get the song name
            play_youtube_video(song_name)  # Play the song

        elif user_input.startswith("open "):
            website_name = user_input[5:]  # Extract website name (e.g., Amazon, Google)
            search_query = input(f"What would you like to search on {website_name.capitalize()}? ")
            open_website_with_search(website_name, search_query)  # Search the website

        elif "cpu usage" in user_input:
            status = get_cpu_usage()
            print(f"Jarvis: {status}")
            # Speak in a separate thread
            threading.Thread(target=lambda: asyncio.run(speak_text(status))).start()

        elif user_input == "list calendar":
            list_events()
            # Speak in a separate thread
            threading.Thread(target=lambda: asyncio.run(speak_text("Here are your calendar events."))).start()

        elif user_input.startswith("add event"):
            summary = input("Enter event name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM, 24-hour format): ")
            add_event(summary, date, time)
            # Speak in a separate thread
            threading.Thread(target=lambda: asyncio.run(speak_text(f"Event {summary} added to your calendar."))).start()

        elif user_input == "exit":
            print("Jarvis: Goodbye!")
            # Speak in a separate thread
            threading.Thread(target=lambda: asyncio.run(speak_text("Goodbye!"))).start()
            break

        else:
            # Default to LLM for unknown requests
            try:
                llm_response = get_assistant_reply(user_input)
                print(f"Jarvis: {llm_response}")
                # Speak in a separate thread
                threading.Thread(target=lambda: asyncio.run(speak_text(llm_response))).start()
            except Exception as e:
                print(f"Jarvis: Sorry, I couldn't process your request. Error: {e}")
                # Speak in a separate thread
                threading.Thread(target=lambda: asyncio.run(speak_text("Sorry, I couldn't process your request."))).start()

if __name__ == "__main__":
    asyncio.run(jarvis())  # Run the jarvis function using an event loop
