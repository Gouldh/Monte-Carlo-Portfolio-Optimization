# Portfolio Optimization Using Monte Carlo Simulation

## Project Overview
This repository contains a powerful investment analysis tool designed to optimize asset allocation by employing Monte Carlo simulations. The tool forecasts 100,000 portfolio scenarios using historical market data to enhance risk-adjusted returns. The tool is implemented in Python and uses libraries such as `yfinance` for data acquisition, `numpy` for numerical computations, and `pandas` for data structuring.

## Features
- **Monte Carlo Simulation**: Generates a multitude of portfolio scenarios to forecast potential future performance.
- **Data Acquisition**: Utilizes `yfinance` to fetch historical market data.
- **Numerical Analysis**: Leverages `numpy` for efficient calculations related to portfolio optimization.
- **Data Structuring**: Employs `pandas` for organizing and handling financial datasets.
- **Efficient Frontier Visualization**: Plots the Efficient Frontier using `matplotlib`, aiding in the identification of the optimal portfolio.
- **Investment Strategy Evaluation**: Calculates Sharpe ratios and volatility measures to guide strategic asset distribution, aiming to outperform benchmark market indices.

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

Ensure your Python environment includes all necessary libraries, such as `yfinance`, `numpy`, `pandas`, and `matplotlib`, for full functionality.

## License
This project is open-sourced under the MIT License. See the `LICENSE` file for more details.


