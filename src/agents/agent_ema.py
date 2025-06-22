import yfinance as yf
import pandas as pd

def fetch_ema_data(symbol="BTC-USD", interval="15m", period="2d"):
    df = yf.download(tickers=symbol, interval=interval, period=period, progress=False)

    if df.empty:
        print("❌ Hiba: üres adat.")
        return None, "neutral"

    df["EMA_5"] = df["Close"].ewm(span=5).mean()
    df["EMA_13"] = df["Close"].ewm(span=13).mean()
    df["EMA_62"] = df["Close"].ewm(span=62).mean()

    # Csak a legutolsó gyertya alapján döntünk:
    ema5 = df["EMA_5"].iloc[-1]
    ema13 = df["EMA_13"].iloc[-1]
    ema62 = df["EMA_62"].iloc[-1]

    if ema5 > ema13 and ema13 > ema62:
        signal = "buy"
    elif ema5 < ema13 and ema13 < ema62:
        signal = "sell"
    else:
        signal = "neutral"

    return df.iloc[-1][["Close", "EMA_5", "EMA_13", "EMA_62"]], signal
