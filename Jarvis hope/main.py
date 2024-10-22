import json
import os
from wikipedia_search import get_wikipedia_answer
from weather_info import get_weather

# File path for storing questions and answers
QA_FILE = "qa_data.json"

# Function to load questions and answers from a JSON file
def load_qa_data():
    if os.path.exists(QA_FILE):
        with open(QA_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save questions and answers to a JSON file
def save_qa_data(data):
    with open(QA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Main function to run Jarvis
def jarvis():
    qa_data = load_qa_data()  # Load existing QA data

    while True:
        user_input = input("You: ").lower()

        # Check if the user input matches any existing question
        if user_input in qa_data:
            print(f"Jarvis: {qa_data[user_input]}")
            continue

        # Handle Wikipedia queries
        if any(user_input.startswith(starter) for starter in ["what", "who", "where", "when", "why"]):
            query = user_input
            result = get_wikipedia_answer(query)
            print(f"Jarvis: {result}")

            # Save the question and answer to the JSON file
            qa_data[user_input] = result
            save_qa_data(qa_data)



        # Handle weather queries
        elif "weather" in user_input:
            city = user_input.replace("weather", "").strip()
            result = get_weather(city)
            print(f"Jarvis: The temperature in {city} is {result}.")

        elif "exit" in user_input:
            print("Jarvis: Goodbye!")
            break

        else:
            print("Jarvis: I'm not sure how to handle that request.")

if __name__ == "__main__":
    jarvis()
