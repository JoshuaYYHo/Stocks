#packages
import yfinance as yf
from pandas import DataFrame as df
import matplotlib.pyplot as pyplot

#maybe use TKinter after this


#this is an object
symbol = yf.Ticker("MSFT")
infos = symbol.info
#pandas data frame
bro = yf.download('MSFT', '2002-01-01', '2022-01-01')

open_bro = bro["Open"]

pyplot.plot(open_bro)
pyplot.xlabel("Open")
pyplot.show()

print(open_bro)