def run():
    print("🚀 run() elindult!")

    from core.fetch_binance import get_order_book
    from core.orderbook_utils import load_orderbook_from_file, calculate_orderbook_metrics
    from agents.agent_orderbook import evaluate_orderbook_signal
    from agents.agent_ema import fetch_ema_data
    from agents.agent_decision_engine import decide_final_signal
    from agents.agent_feedback_manager import log_trade_decision

    print("📡 Lekérjük az order book adatokat a Binance API-ból...")
    orderbook = get_order_book("BTCUSDT", limit=20)

    if orderbook:
        print("\n📈 Top 3 vételi ajánlat:")
        for bid in orderbook["bids"][:3]:
            print(f"💰 Ár: {bid[0]} – Mennyiség: {bid[1]}")

    bids, asks, timestamp = load_orderbook_from_file("data/raw/orderbook_btcusdt.json")
    print(f"\n📅 Időbélyeg: {timestamp}")
    metrics = calculate_orderbook_metrics(bids, asks)
    print("\n📊 Order Book metrikák:")
    for k, v in metrics.items():
        print(f"{k}: {v:.2f}")

    orderbook_signal = evaluate_orderbook_signal(metrics)
    print(f"\n📡 Order Book Ágens jelzése: {orderbook_signal.upper()}")

    ema_data, ema_signal = fetch_ema_data()
    if ema_data is not None:
        print("\n📈 EMA adatok (utolsó gyertya):")
        print(ema_data)
        print(f"📡 EMA Ágens jelzése: {ema_signal.upper()}")

    all_signals = {
        "orderbook": orderbook_signal,
        "ema": ema_signal
    }

    final_signal = decide_final_signal(all_signals)
    print(f"\n🧠 Végső döntés: {final_signal.upper()}")

    # 🔁 EMA-k bekerülnek a naplóba
    market_snapshot = {
        "price": float(ema_data["Close"].iloc[0]),
        "imbalance": float(metrics["imbalance"]),
        "ema_5": float(ema_data["EMA_5"].iloc[0]),
        "ema_13": float(ema_data["EMA_13"].iloc[0]),
        "ema_62": float(ema_data["EMA_62"].iloc[0])
    }

    log_trade_decision(
        signal=final_signal,
        signals_by_agent=all_signals,
        market_data=market_snapshot,
        json_path="logs/prediction_log.jsonl",
        csv_path="logs/feedback_dataset.csv"
    )

if __name__ == "__main__":
    run()
