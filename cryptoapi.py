import requests

url = "https://cryptoapi12.p.rapidapi.com/profit-loss-calculator"

querystring = {"crypto_name":"ethereum","amount":"5","purchase_price":"1650","operation":"long"}

headers = {
	"X-RapidAPI-Key": "75f9271522msh503c12e57ed7833p10fbf9jsn85b2381f5faa",
	"X-RapidAPI-Host": "cryptoapi12.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())