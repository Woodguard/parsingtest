import requests
from apikey import API_TOKEN

params = {"q": "Самара", "appid": API_TOKEN, "units": "metric"}

responce = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

# print(responce.status_code)
# print(responce.headers)
# print(responce.text)
print(responce.json())
