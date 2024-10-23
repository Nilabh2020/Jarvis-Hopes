import json
from wikipedia_search import get_wikipedia_answer
from weather_info import get_weather
from jarvis_learn import jarvis_learn, load_predefined_data

# Load predefined data globally
predefined_data = load_predefined_data()


def jarvis():
    global predefined_data  # Declare it as global so it can be modified inside the function

    while True:
        user_input = input("You: ").lower().strip()

        # Handle learning process
        if "learn" in user_input:
            predefined_data = jarvis_learn(predefined_data)

        # Check if question is in predefined data
        elif user_input in predefined_data:
            print(f"Jarvis: {predefined_data[user_input]}")

        # Wikipedia search
        elif "what is" in user_input or "who is" in user_input or "when" in user_input or "where" in user_input:
            result = get_wikipedia_answer(user_input)
            print(f"Jarvis: {result}")

        # Handle weather queries
        elif "weather" in user_input:
            city = user_input.replace("weather", "").strip()
            result = get_weather(city)
            print(f"Jarvis: {result}")

        # Handle exit
        elif "exit" in user_input:
            print("Jarvis: Goodbye!")
            break

        else:
            print("Jarvis: I'm not sure how to handle that request.")


if __name__ == "__main__":
    jarvis()
