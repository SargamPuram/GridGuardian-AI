import pandas as pd
from google.cloud import bigquery
from config import GCP_PROJECT_ID, BIGQUERY_DATASET

def simulate_sensor_data():
    # Fake simulation of sensor reading
    df = pd.DataFrame({
        'timestamp': pd.date_range('2025-10-01', periods=24, freq='H'),
        'solar_irradiance': np.random.uniform(300, 900, 24),
        'wind_speed': np.random.uniform(2, 12, 24),
        'battery_temp': np.random.uniform(25, 45, 24)
    })
    df.to_csv("../simulated_data/sensor_stream.csv", index=False)
    print("Sensor data simulated and saved.")

def post_to_bigquery():
    client = bigquery.Client(project=GCP_PROJECT_ID)
    table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET}.sensor_data"
    df = pd.read_csv("../simulated_data/sensor_stream.csv")
    job = client.load_table_from_dataframe(df, table_id)
    job.result()
    print(f"Loaded data into {table_id}")

if __name__ == "__main__":
    simulate_sensor_data()
    post_to_bigquery()
