import requests
from bs4 import BeautifulSoup

url = 'https://www.coinmarketcap.com/'
request = requests.get(url)
coin_list = []
soup = BeautifulSoup(request.text, 'html')
for item in soup.find_all('span', class_="crypto-symbol"):
    coin = item.text.strip()
    coin_list.append(coin)
print(coin_list)
