import yfinance as yf
import pandas as pd


def get_financial_data(ticker, period="max", interval="1d"):
    data = yf.download(tickers=ticker, period=period, interval=interval)
    return data
