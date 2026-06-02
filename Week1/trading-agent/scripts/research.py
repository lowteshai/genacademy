# scripts/research.py

import os
import requests
from datetime import datetime, timedelta
import json

ALPACA_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_BASE_URL")

def get_bars(symbol, timeframe="1Day", limit=60):
    """Fetch historical price bars for a symbol."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"https://data.alpaca.markets/v2/stocks/{symbol}/bars"
    # start ~90 calendar days back gives ~60 trading days for MA computation
    start = (datetime.utcnow() - timedelta(days=90)).strftime("%Y-%m-%d")
    params = {
        "timeframe": timeframe,
        "limit": limit,
        "adjustment": "raw",
        "start": start,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_account():
    """Get current portfolio status."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"{BASE_URL}/v2/account"
    response = requests.get(url, headers=headers)
    return response.json()

def get_positions():
    """Get all open positions."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"{BASE_URL}/v2/positions"
    response = requests.get(url, headers=headers)
    return response.json()

def get_news(symbol):
    """Get recent news for a symbol."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"https://data.alpaca.markets/v1beta1/news"
    params = {
        "symbols": symbol,
        "limit": 5,
        "sort": "desc"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_most_actives(top=20):
    """Get most active stocks by volume."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = "https://data.alpaca.markets/v1beta1/screener/stocks/most-actives"
    params = {"by": "trades", "top": top}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_movers(top=20):
    """Get top gainers and losers."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = "https://data.alpaca.markets/v1beta1/screener/stocks/movers"
    params = {"top": top}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_snapshot(symbol):
    """Get latest quote/trade snapshot for a symbol."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"https://data.alpaca.markets/v2/stocks/{symbol}/snapshot"
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "account"
    symbol = sys.argv[2] if len(sys.argv) > 2 else None
    
    if action == "bars" and symbol:
        print(json.dumps(get_bars(symbol)))
    elif action == "news" and symbol:
        print(json.dumps(get_news(symbol)))
    elif action == "positions":
        print(json.dumps(get_positions()))
    elif action == "most-actives":
        print(json.dumps(get_most_actives()))
    elif action == "movers":
        print(json.dumps(get_movers()))
    elif action == "snapshot" and symbol:
        print(json.dumps(get_snapshot(symbol)))
    else:
        print(json.dumps(get_account()))