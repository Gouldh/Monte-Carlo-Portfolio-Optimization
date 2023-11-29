# Portfolio Optimization Using Monte Carlo Simulation

## Project Overview
This project is an investment analysis tool designed to optimize asset allocation by employing Monte Carlo simulations. The tool forecasts 100,000 portfolio scenarios using historical market data to enhance risk-adjusted returns.

## Features
- **Monte Carlo Simulation**: Generates a multitude of portfolio scenarios to forecast potential future performance.
- **Data Acquisition**: Utilizes `yfinance` to fetch historical market data.
- **Numerical Analysis**: Leverages `numpy` for efficient calculations related to portfolio optimization.
- **Data Structuring**: Employs `pandas` for organizing and handling financial datasets.
- **Efficient Frontier Visualization**: Plots the Efficient Frontier using `matplotlib`, aiding in the identification of the optimal portfolio.
- **Investment Strategy Evaluation**: Calculates Sharpe ratios and volatility measures to guide strategic asset distribution, aiming to outperform benchmark market indices.

## Libraries
- `numpy`: Utilized for array and numerical computations. It is particularly used during the Monte Carlo simulation for optimizing performance.
- `pandas`: Used for data transformations. Creates easier handling of Monte Carlo simulation results.
- `yfinance`: Primary source for downloading stock market data. Used for finding asset data for portfolio that will be optimized.
- `matplotlib`: Crucial for data visualization. Used to show the Efficient Frontier and multitude of simulated portfolios.

## Installation
To get started with this portfolio optimization tool, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Gouldh/Monte-Carlo-Portfolio-Optimization.git
   ```
2. Navigate to the repository's directory:
   ```bash
   cd Monte-Carlo-Portfolio-Optimization
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
Execute the `main.py` script to perform the portfolio optimization simulation:

```bash
python main.py
```

## Sample Output
Below is an example of the output produced by running the code with sample input parameters. The Chart shows the return and volatility of the 100,000 portfolios against the market representation (SPY) and provides metrics for the optimized portfolio's performance and the market's performance.

![Example Output](https://github.com/Gouldh/Monte-Carlo-Portfolio-Optimization/blob/main/Monte%20Carlo%20Portfolio%20Optimization%20Example%20Output.png)

## License
This project is open-sourced under the MIT License. See the `LICENSE` file for more details.

**Author**: Hunter Gould         
**Date**: 10/31/2023
