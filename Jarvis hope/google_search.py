# google_search.py
import requests
from bs4 import BeautifulSoup


def google_search(query):
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    # Try getting a more detailed description or snippet along with the title
    first_result_title = soup.find('h3')
    first_result_snippet = soup.find('div', class_='BNeawe s3v9rd AP7Wnd')

    if first_result_title and first_result_snippet:
        return f"{first_result_title.get_text()} - {first_result_snippet.get_text()}"
    elif first_result_title:
        return first_result_title.get_text()
    else:
        return "Sorry, I couldn't find any results."
