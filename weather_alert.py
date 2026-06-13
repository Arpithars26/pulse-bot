import requests
import os

API_KEY = os.environ["OPENWEATHER_API_KEY"]

CITY = "Kochi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

data = requests.get(url).json()

temp = data["main"]["temp"]

print("City:", CITY)
print("Temperature:", temp)

if temp > 35:
    print("WEATHER ALERT")
else:
    print("NO ALERT")