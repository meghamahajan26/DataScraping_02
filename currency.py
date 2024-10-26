import requests as rq

cUrl = "https://api.coinbase.com/v2/exchange-rates"

cHeaders = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

stockData = [
    {
        'name': 'TCS',
        'current_price': 3000,
        'currency': 'INR',
        'Con_price': '?'
    },
    {
        'name': 'GOOG',
        'current_price': 166,
        'currency': 'USD',
        'Con_price': '?'
    },
    {
        'name': 'DBS_group',
        'current_price': 39.18,
        'currency': 'SGD',
        'Con_price': '?'
    },
    {
        'name': 'Trident',
        'current_price': 158.52,
        'currency': 'CNY',
        'Con_price': '?'
    }
]

cResp = rq.get(url=cUrl, headers=cHeaders).json()
currencyData = cResp['data']['rates']

def convert_currency(currencyData):
    for stocks in stockData:
        currency = stocks['currency']
        price = stocks['current_price']

        if currency == 'INR':
            con_rate = float(currencyData['INR'])
            stocks['Con_price'] = round(price / con_rate, 2)
        elif currency in currencyData:
            con_rate = float(currencyData[currency])
            stocks['Con_price'] = round(price * con_rate, 2)
        else: 
            stocks['Con_price'] = 'Rates are not in the list'

convert_currency(currencyData)

for stocks in stockData:
    print(f"name = {stocks['name']}, current_price = {stocks['current_price']}, currency = {stocks['currency']}, Con_price = {stocks['Con_price']}")
