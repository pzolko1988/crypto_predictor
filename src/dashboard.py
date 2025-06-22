import pandas as pd
import plotly.graph_objs as go
from dash import Dash, html, dcc
import os

# Alkalmazás inicializálása
app = Dash(__name__)
app.title = "Predikciós Vizualizáció"

# CSV útvonal
CSV_PATH = "logs/feedback_dataset.csv"

# Adatok beolvasása, ha létezik a fájl
if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
    df = df.tail(50)  # Csak az utolsó 50 sor jelenik meg
else:
    df = pd.DataFrame()

# Grafikon összeállítása
fig = go.Figure()

if not df.empty:
    # Ár
    fig.add_trace(go.Scatter(x=df["timestamp"], y=df["price"], mode="lines+markers", name="Price"))
    # EMA-k
    fig.add_trace(go.Scatter(x=df["timestamp"], y=df["ema_5"], mode="lines", name="EMA 5"))
    fig.add_trace(go.Scatter(x=df["timestamp"], y=df["ema_13"], mode="lines", name="EMA 13"))
    fig.add_trace(go.Scatter(x=df["timestamp"], y=df["ema_62"], mode="lines", name="EMA 62"))

    # Buy/Sell szignálok megjelenítése
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["price"],
        mode="markers",
        marker=dict(
            size=10,
            color=["green" if s == "buy" else "red" for s in df["final_signal"]],
            symbol=["triangle-up" if s == "buy" else "triangle-down" for s in df["final_signal"]]
        ),
        name="Signal"
    ))

# Layout testreszabása
fig.update_layout(
    title="📈 Ár és EMA mozgóátlagok",
    xaxis_title="Idő",
    yaxis_title="Ár (USDT)",
    height=600
)

# Dash megjelenítés
app.layout = html.Div([
    html.H1("📊 Predikciós Vizualizáció", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

# Szerver indítása
if __name__ == "__main__":
    app.run(debug=True)


