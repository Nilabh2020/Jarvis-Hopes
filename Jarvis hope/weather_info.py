import requests
from bs4 import BeautifulSoup

def get_weather(city):
    city = city.replace(' ', '+')
    url = f"https://www.google.com/search?q=weather+{city}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    weather_data = soup.find('div', class_='BNeawe iBp4i AP7Wnd')  # Updated class for temperature
    if weather_data:
        return f"The temperature in {city.replace('+', ' ')} is {weather_data.get_text()}."
    else:
        return "Weather data not available."
