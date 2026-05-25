import requests
import pandas as pd
from datetime import datetime

# Honolulu, HI coordinates — change these to any city you want
LATITUDE = 21.3069
LONGITUDE = -157.8583
CITY_NAME = "Honolulu, HI"

def extract_weather():
    """
    Fetches hourly weather data from the Open-Meteo API.
    No API key needed — completely free.
    Returns a pandas DataFrame with raw weather data.
    """

    url = "https://api.open-meteo.com/v1/forecast"

    # These are the fields we want back from the API
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "forecast_days": 7,  # get 7 days of data
    }

    print(f"Extracting weather data for {CITY_NAME}...")

    response = requests.get(url, params=params)

    # If the API call fails, this will raise an error with details
    response.raise_for_status()

    data = response.json()

    # The API returns lists for each field — zip them together into rows
    df = pd.DataFrame({
        "timestamp": data["hourly"]["time"],
        "temperature_f": data["hourly"]["temperature_2m"],
        "humidity_pct": data["hourly"]["relative_humidity_2m"],
        "wind_speed_mph": data["hourly"]["wind_speed_10m"],
    })

    print(f"  Extracted {len(df)} rows of raw data.")
    return df
