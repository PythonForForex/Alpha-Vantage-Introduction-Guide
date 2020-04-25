from alpha_vantage.foreignexchange import ForeignExchange

app = ForeignExchange(output_format='pandas')

eurusd = app.get_currency_exchange_intraday('EUR', 'USD')

print(eurusd[0])
print(eurusd[0]['2020-04-03']) #Narrow output to specific date