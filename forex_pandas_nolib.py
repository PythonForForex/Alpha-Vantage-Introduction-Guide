import os
import requests
import pandas as pd 

api_key = os.getenv('ALPHAVANTAGE_API_KEY')

base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'FX_INTRADAY',
		 'from_symbol': 'EUR',
		 'to_symbol': 'USD', 
		 'interval': '15min',
		 'apikey': api_key}

response = requests.get(base_url, params=params)
response_dict = response.json()
_, header = response.json()

#Convert to pandas dataframe
df = pd.DataFrame.from_dict(response_dict[header], orient='index')

#Clean up column names
df_cols = [i.split(' ')[1] for i in df.columns]
df.columns = df_cols

print(df)