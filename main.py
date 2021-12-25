import yfinance as yf
from get_all_tickers import get_tickers as gt

list_tickers = gt.get_tickers()
print(list_tickers)
#this is an object
msft = yf.Ticker("MSFT")

print(msft.info)