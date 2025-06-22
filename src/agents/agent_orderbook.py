# src/agents/agent_orderbook.py

def evaluate_orderbook_signal(metrics, threshold=0.1):
    """
    Egyszerű döntéshozatal az order book egyensúly alapján.
    
    :param metrics: dict - tartalmazza a 'imbalance' értéket
    :param threshold: float - minimális elmozdulás, amit már jelzésnek tekintünk
    :return: str - 'buy', 'sell' vagy 'neutral'
    """
    imbalance = metrics.get("imbalance", 0)

    if imbalance > threshold:
        return "buy"
    elif imbalance < -threshold:
        return "sell"
    else:
        return "neutral"
