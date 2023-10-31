import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------------
# Author: Hunter Gould
# Date: 10/31/23
# Description: This project involves portfolio optimization using Monte Carlo simulation
#              to identify an optimal investment portfolio that maximizes returns while
#              minimizing risk. The project is an application of Modern Portfolio
#              Theory and the concept of the Efficient Frontier.
#
# Note: Remember that past performance is not indicative of future results. Risk reduction
#       can be assessed by comparing the volatility of the optimal portfolio with the
#       initial portfolio or a benchmark.
# -----------------------------------------------------------------------------------

ASSETS = ['AAPL', 'MSFT', 'AGG', 'GLD']  # Example assets
START_DATE = '2020-01-01'
END_DATE = '2023-01-01'
MARKET_REPRESENTATION = 'SPY'
NUM_PORTFOLIOS = 10_000
RISK_FREE_RATE = 0  # Assuming risk-free rate is 0 for simplicity


# Data Collection for Assets
data = yf.download(ASSETS, start=START_DATE, end=END_DATE)['Adj Close']

# Data Collection for Market (SPY)
market_data = yf.download(MARKET_REPRESENTATION, start=START_DATE, end=END_DATE)['Adj Close']

# Calculate daily returns
daily_returns = data.pct_change().dropna()

# Create a covariance matrix
cov_matrix = daily_returns.cov()

# Calculating Market Performance (SPY)
market_daily_returns = market_data.pct_change().dropna()
market_return = market_daily_returns.mean() * 252  # Annualized return
market_volatility = market_daily_returns.std() * np.sqrt(252)  # Annualized volatility
market_sharpe_ratio = (market_return - RISK_FREE_RATE) / market_volatility  # Sharpe ratio

# Monte Carlo Simulation
results = np.zeros((4, NUM_PORTFOLIOS))
weights_record = np.zeros((len(ASSETS), NUM_PORTFOLIOS))

for i in range(NUM_PORTFOLIOS):
    # Random weights
    weights = np.random.random(len(ASSETS))
    weights /= np.sum(weights)
    weights_record[:, i] = weights

    # Annualized portfolio return
    portfolio_return = np.sum(weights * daily_returns.mean()) * 252

    # Annualized portfolio volatility
    portfolio_stddev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)

    # Sharpe ratio (assuming risk-free rate is 0 for simplicity)
    sharpe_ratio = (portfolio_return - RISK_FREE_RATE) / portfolio_stddev

    results[0, i] = portfolio_return
    results[1, i] = portfolio_stddev
    results[2, i] = sharpe_ratio
    results[3, i] = i  # Index of the simulation

# Convert results to a DataFrame
columns = ['Return', 'Volatility', 'Sharpe Ratio', 'Simulation']
simulated_portfolios = pd.DataFrame(results.T, columns=columns)

# Find the portfolio with the highest Sharpe ratio
optimal_idx = simulated_portfolios['Sharpe Ratio'].idxmax()
optimal_portfolio = simulated_portfolios.loc[optimal_idx]
optimal_weights = weights_record[:, optimal_idx]

# Visualization
plt.figure(figsize=(12, 8))
plt.scatter(simulated_portfolios['Volatility'], simulated_portfolios['Return'], c=simulated_portfolios['Sharpe Ratio'], cmap='YlGnBu')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.title('Efficient Frontier')
plt.scatter(market_volatility, market_return, color='red', marker='o', s=100)  # Mark the market (SPY) performance
plt.scatter(optimal_portfolio[1], optimal_portfolio[0], color='green', marker='*', s=100)  # Mark the optimal portfolio

# Displaying the weights of each item in the optimal portfolio
weight_text = "Optimal Weights:\n" + '\n'.join([f"{asset}: {weight*100:.2f}%" for asset, weight in zip(ASSETS, optimal_weights)])
plt.gcf().text(0.14, 0.86, weight_text, fontsize=10, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'), ha='left')

# Displaying Optimized Portfolio Performance
optimal_text = f"Optimized Portfolio\nReturn: {optimal_portfolio['Return'] * 100:.2f}%\nVolatility: {optimal_portfolio['Volatility'] * 100:.2f}%\nSharpe Ratio: {optimal_portfolio['Sharpe Ratio']:.2f}"
plt.gcf().text(0.14, 0.74, optimal_text, fontsize=10, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='green', facecolor='white'), ha='left')

# Displaying Market (SPY) Performance
market_text = f"Market (SPY)\nReturn: {market_return * 100:.2f}%\nVolatility: {market_volatility * 100:.2f}%\nSharpe Ratio: {market_sharpe_ratio:.2f}"
plt.gcf().text(0.14, 0.64, market_text, fontsize=10, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='red', facecolor='white'), ha='left')

# Display Full Chart
plt.show()
