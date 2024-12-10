import webbrowser

# Predefined website URLs with search parameters
websites = {
    "google": "https://www.google.com/search?q=",
    "amazon": "https://www.amazon.in/s?k=",
    "youtube": "https://www.youtube.com/results?search_query=",
    "bing": "https://www.bing.com/search?q=",
    "flipcart": "https://www.flipkart.com/",
}

def open_website_with_search(website_name, search_query):
    # Check if the website is predefined in the dictionary
    if website_name.lower() in websites:
        search_url = websites[website_name.lower()] + search_query.replace(" ", "+")
        webbrowser.open(search_url)  # Opens the URL in the default web browser
    else:
        print(f"Sorry, I can't open {website_name}. Please add it to the list.")
