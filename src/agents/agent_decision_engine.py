# src/agents/agent_decision_engine.py

def decide_final_signal(signals, priority_order=None):
    """
    Összesíti az ágensek kimeneteit, és döntést hoz.

    :param signals: dict, pl. {"orderbook": "buy", "ema": "neutral", ...}
    :param priority_order: list, pl. ["ml", "orderbook", "ema"]
    :return: str - 'buy', 'sell' vagy 'neutral'
    """

    if not signals:
        return "neutral"

    # Alapértelmezett sorrend, ha nincs megadva
    if priority_order is None:
        priority_order = list(signals.keys())

    for key in priority_order:
        signal = signals.get(key)
        if signal in ["buy", "sell"]:
            return signal

    return "neutral"
