import requests

API_KEY = "d1448050863d5bba7e55d44879cc3ab0"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if data.get("cod") != 200:
        print("Error:", data.get("message"))
        return
    
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    rain = data.get("rain", {}).get("1h", 0)  

    print(f"\nWeather in {city}: {weather}, {temp}°C")
    
    
    if rain > 0:
        print("🌧 Rain expected – avoid sowing or spraying pesticides today.")
    elif temp > 35:
        print("🔥 Very hot – irrigate crops to avoid heat stress.")
    else:
        print("✅ Weather looks fine for farming activities.")

# Demo
city = input("Enter city/village: ")
get_weather(city)
