from alpha_vantage.techindicators import TechIndicators

app = TechIndicators(output_format='pandas')
#help(app.get_macd)

aapl_macd = app.get_macd('aapl', fastperiod=12, slowperiod=26, signalperiod=9)
print(aapl_macd)