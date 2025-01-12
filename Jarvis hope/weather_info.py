import requests
from bs4 import BeautifulSoup

def get_weather(city):
    # Replace spaces in the city name to + for the search query
    city = city.replace(' ', '+')
    url = f"https://www.google.com/search?q=weather+{city}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Send a request to Google search page
    response = requests.get(url, headers=headers)

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the weather information
    try:
        weather_data = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
        temperature = weather_data.get_text()
        return f"The temperature in {city.replace('+', ' ')} is {temperature}."
    except AttributeError:
        return "Sorry, I couldn't find the weather data for that city."
