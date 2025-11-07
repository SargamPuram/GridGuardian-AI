import dash
from dash import html, dcc
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv("../simulated_data/failure_forecast.csv")

app.layout = html.Div([
    html.H1("GridGuardian AI: NEOM Grid Monitor"),
    dcc.Graph(
        figure={
            "data": [
                {"x": df["timestamp"], "y": df["solar_irradiance"], "type": "line", "name": "Solar Irradiance"},
                {"x": df["timestamp"], "y": df["battery_temp"], "type": "line", "name": "Battery Temp"},
            ],
            "layout": {"title": "Simulated Sensor Readings"}
        }
    ),
    dcc.Markdown("### Failure Risk Timeline"),
    dcc.Graph(
        figure={
            "data": [
                {"x": df["timestamp"], "y": df["failure_risk"].astype(int), "type": "bar", "name": "Failure Risk"}
            ],
            "layout": {"yaxis": {"title": "Failure Risk (1=High)"}}
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
