from alpha_vantage.timeseries import TimeSeries

app = TimeSeries() #Default - JSON format
#Valid options for output_format are 'pandas', 'csv'.
#app = TimeSeries(output_format='pandas')
#app = TimeSeries(output_format='csv')

help(app)

aapl = app.get_daily_adjusted('BTCUSD', outputsize='full')
print(aapl)