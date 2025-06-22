# src/core/fetch_binance.py

import requests
import json
from datetime import datetime

def get_order_book(symbol="BTCUSDT", limit=20):
    url = "https://api.binance.com/api/v3/depth"
    params = {
        "symbol": symbol.upper(),
        "limit": limit
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Időbélyeg hozzáadása
        data["timestamp"] = datetime.utcnow().isoformat()

        # Mentés a raw mappába
        filepath = f"data/raw/orderbook_{symbol.lower()}.json"
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

        print(f"🔄 Order book letöltve: {filepath}")
        return data

    except requests.exceptions.RequestException as e:
        print(f"❌ Hiba: {e}")
        return None
