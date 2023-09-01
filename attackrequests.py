import requests

def attack():
    url = 'https://www.coinmarketcap.com/'
    request = requests.get(url)
    print(request)
    attack()

attack()