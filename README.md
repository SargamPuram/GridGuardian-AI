# GridGuardian AI: Predictive Resilience for NEOM’s Renewable Grid

GridGuardian AI is an end-to-end solution to anticipate, analyze, and respond to failure risks across NEOM’s 100% renewable smart grid. Built using Google Cloud (Vertex AI, Gemini, BigQuery, IoT Core), the project ingests, processes, and visualizes real-world weather and grid telemetry data.
- **AI Forecasting models:** Vertex AI for renewable energy and extreme event forecasting.
- **Gemini AI:** Multi-modal analysis for failure mode prediction (satellite, sensors, maintenance logs).
- **Live dashboard:** Real-time status, risk, and recommendations.

---

## How to run

1. Clone this repo and create a `.env` file (see `.env.example`) with your GCP project config and API keys.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Ingest demo data to BigQuery:  
   `python src/ingest_weather.py`
   `python src/ingest_sensors.py`
4. Run forecasting / Gemini analysis:  
   `python src/vertex_forecast.py`
   `python src/gemini_failure_analysis.py`
5. Start dashboard:
   `python src/dashboard_app.py`

---

## Dataset sources
- [KAUST Red Sea Meteorological Data](https://reefecology.kaust.edu.sa/research/detail/biodiversity-of-saudi-arabian-red-sea-coral-reefs)
- [Open Grid Data - Sample Telemetry]

## Technologies
Vertex AI, Gemini AI, BigQuery, IoT Core, Google Maps API, Python, Dash
