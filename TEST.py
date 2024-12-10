import requests

# Define the URL and headers for the API
url = "https://api.x.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer xai-AO88EIqbRpMQaUlBy7BJi1UrhHW74230NV56eI5NwPAldvKtTTceHksdN4NurKrtEJBM0B3vV2oTBWdN"
}


def get_assistant_reply(user_query):
    # Set up the data to be sent in the request
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a test assistant."
            },
            {
                "role": "user",
                "content": user_query  # Use the user's input here
            }
        ],
        "model": "grok-beta",
        "stream": False,
        "temperature": 0
    }

    # Send the POST request to the API
    response = requests.post(url, headers=headers, json=data)

    # Parse the JSON response and get the assistant's content
    response_json = response.json()
    assistant_reply = response_json['choices'][0]['message']['content']
    return assistant_reply


def main():
    print("Welcome to the assistant. Type 'exit' to quit.")

    while True:
        # Take user input for the query
        user_query = input("Enter your query: ")

        # Exit condition
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break

        # Get the assistant's reply
        assistant_reply = get_assistant_reply(user_query)

        # Print the assistant's response
        print(f"Assistant: {assistant_reply}")


if __name__ == "__main__":
    main()
