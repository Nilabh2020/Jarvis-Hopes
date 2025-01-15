# chat_api.py
import requests
import json


def chat_with_ai(number_of_questions=3):
    question_number = 0

    while question_number < number_of_questions:
        question = str(input("Question: "))
        data = {
            "model": "llama3",
            "messages": [{"role": "user", "content": question}],
            "stream": False
        }
        url = "http://localhost:11434/api/chat"
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
            response_json = response.json()  # Parses the JSON response
            ai_reply = response_json.get("message", {}).get("content", "No response from AI.")
            print(ai_reply)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

        question_number += 1
