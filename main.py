import requests
import json

def fetch_weather_data(api_key, location):
    base_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data. Status code: {response.status_code}")
        return None

def display_weather(data):
    if data is None:
        print("Weather data unavailable.")
    else:
        location = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        temp_f = data['current']['temp_f']
        humidity = data['current']['humidity']
        condition = data['current']['condition']['text']

        print(f"Weather for {location}, {region}, {country}:")
        print(f"Condition: {condition}")
        print(f"Temperature: {temp_c}°C / {temp_f}°F")
        print(f"Humidity: {humidity}%")

if __name__ == "__main__":
    api_key = '883651daf912499c87445612242106'  # Replace with your WeatherAPI key
    location = input("Enter a city or ZIP code: ")
    
    weather_data = fetch_weather_data(api_key, location)
    display_weather(weather_data)
