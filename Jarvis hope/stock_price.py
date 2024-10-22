import yfinance as yf

# Dictionary mapping company names to their ticker symbols
company_tickers = {
    "apple": "AAPL",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "amazon": "AMZN",
    "tesla": "TSLA",
    "facebook": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA",
    "twitter": "TWTR",
    "disney": "DIS",
    "berkshire hathaway": "BRK.A",
    "visa": "V",
    "mastercard": "MA",
    "paypal": "PYPL",
    "intel": "INTC",
    "ibm": "IBM",
    "coca-cola": "KO",
    "pepsico": "PEP",
    "exxon mobil": "XOM",
    "johnson & johnson": "JNJ",
    "procter & gamble": "PG",
    "pfizer": "PFE",
    "merck": "MRK",
    "abbvie": "ABBV",
    "3m": "MMM",
    "boeing": "BA",
    "goldman sachs": "GS",
    "american express": "AXP",
    "unitedhealth": "UNH",
    "walmart": "WMT",
    "costco": "COST",
}


def get_stock_price(company):
    company = company.lower()

    # Check if the company is in the dictionary and get the ticker symbol
    ticker = company_tickers.get(company)
    if not ticker:
        return "Company not found. Please try another company."

    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period='1d')['Close'].iloc[-1]
        return f"The current stock price of {company.title()} is ${price:.2f}"
    except Exception as e:
        return "Stock data not available."
