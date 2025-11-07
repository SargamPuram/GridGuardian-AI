import pandas as pd
from google.cloud import bigquery
from config import GCP_PROJECT_ID, BIGQUERY_DATASET

client = bigquery.Client(project=GCP_PROJECT_ID)
weather_df = pd.read_csv('data/red_sea_weather_sample.csv')

table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET}.weather"
job = client.load_table_from_dataframe(weather_df, table_id)
job.result()
print(f"[GridGuardian AI] Weather data from KAUST loaded into {table_id}")

