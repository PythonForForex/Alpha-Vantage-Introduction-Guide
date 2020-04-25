import os
import requests
import pandas as pd

api_key = os.getenv('ALPHAVANTAGE_API_KEY')

base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'FX_INTRADAY',
		 'from_symbol': 'EUR',
		 'to_symbol': 'USD', 
		 'interval': '15min',
		 'datatype': 'csv',
		 'apikey': api_key}

response = requests.get(base_url, params=params)

#Save CSV to file
with open('eurusd.csv', 'wb') as file:
	file.write(response.content)

df = pd.read_csv('eurusd.csv') #Create pandas dataframe

df.set_index('timestamp', inplace=True) #Time-series index

df.to_csv('eurusd.csv') #Save dataframe to csv file