import yfinance as yf
import pandas as pd



ticker = "TSLA"

stock_data = yf.download(tickers=ticker, period="max", interval="1d")

print(stock_data.head(10))
print(len(stock_data))