#!/usr/bin/env python3
"""
Weather App - Created by Genesis AI
"""
import requests
from datetime import datetime

API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str) -> dict:
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "ru"}
    response = requests.get(BASE_URL, params=params)
    return response.json() if response.status_code == 200 else None

def display_weather(data):
    if not data:
        return "Город не найден"
    
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    city = data["name"]
    
    return f"{city}: {temp}°C, {desc}"

if __name__ == "__main__":
    print("Weather App v1.0")
    city = input("Введите город: ")
    print(display_weather(get_weather(city)))
