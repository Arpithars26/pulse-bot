import requests

API_KEY = "52cf7ce7e48d73989979337d1007abc4"
CITY = "Kochi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

temp = data["main"]["temp"]

print("City:", CITY)
print("Temperature:", temp)

if temp > 35:
    print("ALERT: Temperature above 35°C")
else:
    print("Temperature Normal")