import numpy as np

def compute_return(prices):
    return (prices[-1] / prices[0]) - 1

def annualized_return(prices, years):
    return (prices[-1] / prices[0]) ** (1 / years) - 1

def volatility(prices):
    returns = prices.pct_change().dropna()
    return returns.std() * np.sqrt(252)

def sharpe_ratio(prices, risk_free_rate=0.02):
    ann_ret = annualized_return(prices, years=(len(prices) / 252))
    vol = volatility(prices)
    return (ann_ret - risk_free_rate) / vol if vol != 0 else 0
