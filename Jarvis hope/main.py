from google_search import google_search
from wikipedia_search import fetch_wikipedia_summary
from stock_price import get_stock_price
from weather_info import get_weather

def jarvis():
    while True:
        user_input = input("You: ").lower()

        if "google" in user_input:
            query = user_input.replace("google", "").strip()
            result = google_search(query)
            print(f"Jarvis: {result}")

        elif "wikipedia" in user_input:
            query = user_input.replace("wikipedia", "").strip()
            result = fetch_wikipedia_summary(query)
            print(f"Jarvis: {result}")

        elif "stock price" in user_input or "stock" in user_input:
            company = user_input.replace("stock price", "").replace("of", "").strip()
            result = get_stock_price(company)
            print(f"Jarvis: {result}")

        elif "weather" in user_input:
            city = user_input.replace("weather", "").replace("of", "").strip()
            result = get_weather(city)
            print(f"Jarvis: {result}")

        elif "exit" in user_input:
            print("Jarvis: Goodbye!")
            break

        else:
            print("Jarvis: I'm not sure how to handle that request.")

if __name__ == "__main__":
    jarvis()
