import json
import os

# File path for the JSON data
DATA_FILE = 'predefined_data.json'

# Load predefined data from JSON file
def load_predefined_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save predefined data back to JSON file
def save_predefined_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Function to handle the learning process
def jarvis_learn(predefined_data):
    print("Jarvis: Sir, can you tell me the question?")
    question = input("Jarvis Question: ").lower().strip()

    if question in predefined_data:
        print("Jarvis: I already know the answer to this question.")
        return predefined_data

    print("Jarvis: Sir, can you tell me the answer?")
    answer = input("Jarvis Answer: ").strip()

    # Save this new question and answer to predefined data
    predefined_data[question] = answer
    save_predefined_data(predefined_data)

    print("Jarvis: I have learned this new information!")

    return predefined_data
