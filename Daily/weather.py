import requests
from datetime import datetime

def get_weather(api_key, city, state):
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    location = f"{city},{state},US"
    params = {'q': location, 'appid': api_key, 'units': 'imperial'}
    response = requests.get(current_weather_url, params=params).json()
    
    if response.get("cod") != 200:
        print("Error:", response.get("message", "Unknown error"))
        return None
    
    weather_info = {
        "City": response["name"],
        "Temperature (°F)": response["main"]["temp"],
        "Weather": response["weather"][0]["description"],
    }
    
    if "alerts" in response:
        weather_info["Warning"] = response["alerts"][0]["description"]
    
    return weather_info

def get_forecast(api_key, city, state):
    forecast_url = 'https://api.openweathermap.org/data/2.5/forecast'
    location = f"{city},{state},US"
    params = {'q': location, 'appid': api_key, 'units': 'imperial'}
    response = requests.get(forecast_url, params=params).json()
    
    if response.get("cod") != "200":
        print("Error:", response.get("message", "Unknown error"))
        return None
    
    forecast_list = []
    for entry in response["list"][:5]:
        date_time = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
        formatted_time = date_time.strftime("%A, %I:%M %p")
        
        forecast_list.append({
            "Date": formatted_time,
            "Temperature (°F)": entry["main"]["temp"],
            "Weather": entry["weather"][0]["description"],
        })
    return forecast_list

def main():
    api_key = '3da8bb24af6562a8a1a9d2c4464b5f8e'
    city = input("Enter city name: ")
    state = input("Enter state abbreviation (e.g., WA for Washington): ")
    
    weather = get_weather(api_key, city, state)
    if weather:
        print("\nCurrent Weather:")
        for key, value in weather.items():
            print(f"{key}: {value}")
        
        if "Warning" in weather:
            print("\n⚠ Weather Alert: ", weather["Warning"])
    
    forecast = get_forecast(api_key, city, state)
    if forecast:
        print("\n5-Day Forecast:")
        for day in forecast:
            print(f"{day['Date']}: {day['Temperature (°F)']}°F, {day['Weather']}")
    
if __name__ == "__main__":
    main()
