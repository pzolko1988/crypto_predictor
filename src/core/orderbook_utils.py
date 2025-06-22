# src/core/orderbook_utils.py

import json
import pandas as pd

def load_orderbook_from_file(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

    bids = pd.DataFrame(data["bids"], columns=["price", "quantity"], dtype=float)
    asks = pd.DataFrame(data["asks"], columns=["price", "quantity"], dtype=float)

    return bids, asks, data["timestamp"]

def calculate_orderbook_metrics(bids, asks):
    total_bid_qty = bids["quantity"].sum()
    total_ask_qty = asks["quantity"].sum()

    imbalance = (total_bid_qty - total_ask_qty) / (total_bid_qty + total_ask_qty)

    return {
        "total_bid_qty": total_bid_qty,
        "total_ask_qty": total_ask_qty,
        "imbalance": imbalance
    }
