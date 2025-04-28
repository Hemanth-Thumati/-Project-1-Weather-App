import requests

API_KEY = 'your_api_key_here'  # 🔥 Get your free API key from OpenWeatherMap
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # or 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"Weather in {city_name}: {weather['description'].title()}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
    else:
        print("City not found. Please check the spelling!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)