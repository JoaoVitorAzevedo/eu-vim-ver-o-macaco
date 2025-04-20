import yfinance as yf
import pandas as pd

def get_data(tickers, start='2015-01-01', end='2024-01-01'):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    return data.dropna()
