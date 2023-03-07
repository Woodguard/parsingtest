from requests import Session
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0 (Edition Yx GX)"}


work = Session()

work.get("https://quotes.toscrape.com", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

tocen = soup.find("form").find("input").get("value")

data = {"csrf_token": tocen, "username": "username", "password": "password"}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

result = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")

    if len(result) != 0:

    else:
        break
