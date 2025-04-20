from utils.data_loader import get_data
from utils.metrics import compute_return, sharpe_ratio
from strategies.macaco import select_macaco_portfolio

ALL_TICKERS = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA',
               'WEGE3.SA', 'ABEV3.SA', 'MGLU3.SA', 'ELET3.SA', 'LREN3.SA',
               'JBSS3.SA', 'SUZB3.SA', 'CSNA3.SA', 'RENT3.SA']

def run_macaco():
    portfolio = select_macaco_portfolio(ALL_TICKERS, n=5)
    print(f"Carteira do Macaco: {portfolio}")
    data = get_data(portfolio)
    portfolio_value = data.mean(axis=1)
    
    ret = compute_return(portfolio_value)
    sharpe = sharpe_ratio(portfolio_value)

    print(f"Retorno: {ret:.2%}")
    print(f"Sharpe Ratio: {sharpe:.2f}")

if __name__ == '__main__':
    run_macaco()
