import pandas as pd
from google.cloud import bigquery
from config import GCP_PROJECT_ID, BIGQUERY_DATASET

client = bigquery.Client(project=GCP_PROJECT_ID)
telemetry_df = pd.read_csv('data/grid_telemetry.csv')

table_id = f"{GCP_PROJECT_ID}.{BIGQUERY_DATASET}.telemetry"
job = client.load_table_from_dataframe(telemetry_df, table_id)
job.result()
print(f"[GridGuardian AI] Grid telemetry loaded into {table_id}")

