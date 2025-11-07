from google.cloud import aiplatform
from config import GCP_PROJECT_ID, VERTEX_AI_REGION

aiplatform.init(project=GCP_PROJECT_ID, location=VERTEX_AI_REGION)
# Assume model and endpoint are pre-configured in Vertex AI
endpoint = aiplatform.Endpoint("projects/{project}/locations/{location}/endpoints/forecast_endpoint_id")
sample_input = {
    "instances": [
        {"temp": 42, "irradiance": 850, "dust": 78, "wind": 12}
    ]
}
prediction = endpoint.predict(instances=sample_input["instances"])
print("[GridGuardian AI] Vertex AI Forecasting Output:", prediction)
