import requests

# Define the URL and headers for the API
url = "https://api.x.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer xai-AO88EIqbRpMQaUlBy7BJi1UrhHW74230NV56eI5NwPAldvKtTTceHksdN4NurKrtEJBM0B3vV2oTBWdN"
}

def get_assistant_reply(user_query):
    """
    Sends a query to the custom LLM API and retrieves the response.
    """
    data = {
        "messages": [
            {"role": "system", "content": "You are a test assistant."},
            {"role": "user", "content": user_query}
        ],
        "model": "grok-beta",
        "stream": False,
        "temperature": 0
    }

    try:
        # Send the POST request
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        response_json = response.json()
        return response_json['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error communicating with the LLM API: {e}"
