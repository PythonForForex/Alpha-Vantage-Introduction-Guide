import os
import requests

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
print(api_key)

#method 1 - parameters in url
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo')
print(response.json())

#method 2 - using f strings
base_url = 'https://www.alphavantage.co/query?'
function = 'TIME_SERIES_DAILY_ADJUSTED'
symbol = 'IBM'

response = requests.get(f'{base_url}function={function}&symbol={symbol}&apikey={api_key}')
print(response.json())

#method 3 - using a params dictionary ** recommended method
base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
		 'symbol': 'IBM',
		 'apikey': api_key}

response = requests.get(base_url, params=params)
print(response.json())