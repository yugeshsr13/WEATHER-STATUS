import requests
import json
import datetime

def get_coordinates(api_key, city):
    geocoding_url = "https://api.opencagedata.com/geocode/v1/json"
    geocoding_params = {
        "q": city,
        "key": api_key
    }

    geocoding_response = requests.get(geocoding_url, params=geocoding_params)
    geocoding_data = geocoding_response.json()

    if geocoding_data['results']:
        latitude = geocoding_data['results'][0]['geometry']['lat']
        longitude = geocoding_data['results'][0]['geometry']['lng']
        return latitude, longitude
    else:
        return None, None

def get_weather_status(api_key, latitude, longitude, date):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "dt": date
    }

    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)

    if 'main' in weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        print("\n+++ Weather Status +++\n")
        print(f"Location: {city}")
        print(f"Date: {datetime.datetime.fromtimestamp(date)}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("Weather data not available.")

# Replace 'YOUR_GEOCODING_API_KEY' with your actual OpenCage Geocoding API key
geocoding_api_key = 'YOUR_GEOCODING_API_KEY'
# Replace 'YOUR_WEATHER_API_KEY' with your actual OpenWeatherMap API key
weather_api_key = 'YOUR_WEATHER_API_KEY'

city = input("Enter the city name: ")
date_str = input("Enter the date (YYYY-MM-DD): ")
date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
timestamp = int(date_obj.timestamp())

latitude, longitude = get_coordinates(geocoding_api_key, city)

if latitude is not None and longitude is not None:
    get_weather_status(weather_api_key, latitude, longitude, timestamp)
else:
    print("Coordinates not found for the given city.")
