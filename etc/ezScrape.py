import requests
from bs4 import BeautifulSoup

response = requests.request("GET", "https://finance.yahoo.com/cryptocurrencies/")

print(BeautifulSoup(response.text))

