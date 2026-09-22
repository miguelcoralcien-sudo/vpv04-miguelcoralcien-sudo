import requests
url = "https://query1.finance.yahoo.com/v8/finance/chart/KC=F"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebkit/537.36"}
r = requests.get(url,headers=headers)
print("Код ответа:", r.status_code)
data = r.json()
price = data['chart']['result'][0]['meta']['regularMarketPrice'] 
currency = data['chart']['result'][0]['meta']['currency']
print(f"Цена кофе Arabica: {price} {currency}")