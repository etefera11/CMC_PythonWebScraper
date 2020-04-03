from bs4 import BeautifulSoup
import requests
import json
url = 'https://coinmarketcap.com/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

coin = content.findAll('tr', attrs={"class": "cmc-table-row"})
coinArr = []
for coin in content.findAll('tr', attrs={"class": "cmc-table-row"}):
        coinObject = {
            "Name": (coin.find('td', attrs={"class": "cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"})).text,
            "Price": (coin.find('td', attrs={"class": "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"})).text
        }
        coinArr.append(coinObject)
with open('coinData.json','w') as outfile:
    json.dump(coinArr, outfile)