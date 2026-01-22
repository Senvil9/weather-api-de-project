import requests

api_key = "***"
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"  # Changed to HTTPS

def fetch_data():
    print("Starting fetch_data function...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-01-10 23:56', 'localtime_epoch': 1768089360, 'utc_offset': '-5.0'}, 'current': {'observation_time': '04:56 AM', 'temperature': 5, 'weather_code': 143, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png'], 'weather_descriptions': ['Mist'], 'astro': {'sunrise': '07:20 AM', 'sunset': '04:48 PM', 'moonrise': 'No moonrise', 'moonset': '11:07 AM', 'moon_phase': 'Last Quarter', 'moon_illumination': 56}, 'air_quality': {'co': '270.85', 'no2': '39.65', 'o3': '9', 'so2': '6.55', 'pm2_5': '5.85', 'pm10': '6.05', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 10, 'wind_degree': 56, 'wind_dir': 'NE', 'pressure': 1008, 'precip': 0.2, 'humidity': 89, 'cloudcover': 100, 'feelslike': 3, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}} 

