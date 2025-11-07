
import pandas as pd

def simple_forecast():
    df = pd.read_csv("../simulated_data/sensor_stream.csv")
    # Example: predict failures when solar_irradiance < 400 or battery temp > 40
    df['failure_risk'] = ((df['solar_irradiance'] < 400) | (df['battery_temp'] > 40))
    df.to_csv("../simulated_data/failure_forecast.csv", index=False)
    print("Forecast completed and saved.")

if __name__ == "__main__":
    simple_forecast()
