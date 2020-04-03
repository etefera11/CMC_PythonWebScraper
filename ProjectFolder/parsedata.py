import json
with open('coinData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    i['Price'] = i['Price'].replace("$", "")
    i['Price'] = i['Price'].replace(",", "")
    if float(i['Price']) > 1.00:
        print(i['Name'], i['Price'])