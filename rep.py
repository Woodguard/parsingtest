import requests
from apikey import API_TOKEN

params = {"q": "Самара", "appid": API_TOKEN, "units": "metric"}


headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0 (Edition Yx GX)",
    "X-Amzn-Trace-Id": "Root=1-6405b652-7879db4d44f4643d15bea3cc"
  }


responce = requests.get("http://httpbin.org/headers", headers=headers)

print(responce.text)
