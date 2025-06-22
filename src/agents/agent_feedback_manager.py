import json
import pandas as pd
from datetime import datetime
import os

def log_trade_decision(signal, signals_by_agent, market_data, json_path, csv_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Egyetlen naplóbejegyzés, minden mezővel
    log_entry = {
        "timestamp": timestamp,
        "final_signal": signal,
        "orderbook_signal": signals_by_agent.get("orderbook"),
        "ema_signal": signals_by_agent.get("ema"),
        "imbalance": market_data.get("imbalance"),
        "price": market_data.get("price"),
        "ema_5": market_data.get("ema_5"),
        "ema_13": market_data.get("ema_13"),
        "ema_62": market_data.get("ema_62")
    }

    # 1️⃣ JSONL fájlba mentés (soronként egy JSON objektum)
    with open(json_path, "a", encoding="utf-8") as json_file:
        json_file.write(json.dumps(log_entry) + "\n")

    # 2️⃣ CSV fájlba mentés (fejléc csak ha nem létezik)
    df = pd.DataFrame([log_entry])
    write_header = not os.path.exists(csv_path)
    df.to_csv(csv_path, mode="a", index=False, header=write_header)
