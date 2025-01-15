import requests
import json
import time

if __name__ == "__main__":
    number_of_questions = 3
    question_number = 0

    while question_number < number_of_questions:
        question = str(input("Question: "))

        # Start the timer
        start_time = time.time()

        data = {
            "model": "llama3",
            "messages": [{"role": "user", "content": question}],
            "stream": False
        }
        url = "http://localhost:11434/api/chat"

        try:
            response = requests.post(url, json=data)
            response.raise_for_status()

            response_json = response.json()
            full_response = response_json.get("message", {}).get("content", "No valid response received.")

            # End the timer
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Just print the full response (no summarization)
            print(f"Full Response:\n{full_response}\n")
            print(f"Response time: {elapsed_time:.2f} seconds")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

        question_number += 1
