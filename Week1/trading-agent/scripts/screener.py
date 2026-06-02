# scripts/screener.py
# Generates dynamic_watchlist.json each morning from Alpaca screener data.
# Filters: price >= $5, not a warrant/ETN (no W/U suffix), not already in core watchlist.
# Picks top 5 most-actives by trade count + top 3 gainers (capped at 30% move to avoid pumps).

import os
import json
import requests
from datetime import datetime, timezone

ALPACA_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET = os.getenv("APCA_API_SECRET_KEY")
HEADERS = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET,
}
MIN_PRICE = 5.0
MAX_GAINER_PCT = 30.0
ACTIVES_PICK = 2
GAINERS_PICK = 1


def load_core_symbols():
    with open("watchlist.json") as f:
        data = json.load(f)
    return {s["symbol"] for s in data["watchlist"]}


def get_snapshot_price(symbol):
    url = f"https://data.alpaca.markets/v2/stocks/{symbol}/snapshot"
    r = requests.get(url, headers=HEADERS)
    data = r.json()
    try:
        return float(data["latestTrade"]["p"])
    except (KeyError, TypeError):
        return None


def is_valid_symbol(symbol):
    # Skip warrants, rights, ETNs — typically end in W, R, U, Z
    if len(symbol) > 4 and symbol[-1] in ("W", "R", "U", "Z"):
        return False
    return True


def build_dynamic_watchlist():
    core = load_core_symbols()

    # --- Most actives ---
    r = requests.get(
        "https://data.alpaca.markets/v1beta1/screener/stocks/most-actives",
        headers=HEADERS,
        params={"by": "trades", "top": 20},
    )
    actives = r.json().get("most_actives", [])

    active_picks = []
    for entry in actives:
        symbol = entry["symbol"]
        if symbol in core or not is_valid_symbol(symbol):
            continue
        price = get_snapshot_price(symbol)
        if price is None or price < MIN_PRICE:
            continue
        active_picks.append({
            "symbol": symbol,
            "reason": f"top active — {entry['trade_count']:,} trades, vol {entry['volume']:,}",
            "price": price,
        })
        if len(active_picks) >= ACTIVES_PICK:
            break

    # --- Gainers ---
    r = requests.get(
        "https://data.alpaca.markets/v1beta1/screener/stocks/movers",
        headers=HEADERS,
        params={"top": 20},
    )
    gainers = r.json().get("gainers", [])

    gainer_picks = []
    for entry in gainers:
        symbol = entry["symbol"]
        pct = entry["percent_change"]
        price = entry["price"]
        if symbol in core or not is_valid_symbol(symbol):
            continue
        if price < MIN_PRICE or pct > MAX_GAINER_PCT:
            continue
        gainer_picks.append({
            "symbol": symbol,
            "reason": f"top gainer — +{pct:.1f}% today, price ${price:.2f}",
            "price": price,
        })
        if len(gainer_picks) >= GAINERS_PICK:
            break

    # --- Assemble ---
    seen = set()
    dynamic = []
    for pick in active_picks + gainer_picks:
        if pick["symbol"] not in seen:
            seen.add(pick["symbol"])
            dynamic.append({
                "symbol": pick["symbol"],
                "description": pick["reason"],
                "max_allocation_pct": 2,
                "category": "dynamic",
            })

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dynamic_watchlist": dynamic,
    }

    with open("dynamic_watchlist.json", "w") as f:
        json.dump(output, f, indent=2)

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    build_dynamic_watchlist()
