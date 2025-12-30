import requests

API_KEY = "e4eab80d89e1e5a7ec736ccc8880527c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ").strip()


params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    print("\nWeather Information")
    print("-------------------")
    print(f"City        : {data['name']}")
    print(f"Temperature : {data['main']['temp']}°C")
    print(f"Humidity    : {data['main']['humidity']}%")
    print(f"Condition   : {data['weather'][0]['description'].capitalize()}")
else:
    print("Error fetching weather data")
    print("API message:", data.get("message"))
