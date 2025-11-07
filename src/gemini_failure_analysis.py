import requests
import json
from config import GEMINI_API_KEY

def run_gemini_multimodal_analysis(sensor_data, image_url, logs):
    api_url = "https://api.gemini.google.com/v1/multimodal/analyze"
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    payload = {
        "sensor_stream": sensor_data,
        "satellite_image": image_url,
        "maintenance_logs": logs
    }
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    # Example: Load fake inputs for demo
    with open('../data/grid_telemetry.csv') as f:
        sensor_data = f.read()
    image_url = "https://reefecology.kaust.edu.sa/media/satellite_sample.png"
    logs = "2025-10-03: Inverter temp anomaly; 2025-10-01: Dust cleaning cycle"

    output = run_gemini_multimodal_analysis(sensor_data, image_url, logs)
    print("[GridGuardian AI] Gemini Failure Analysis Output:", output)
