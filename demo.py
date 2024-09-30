"""
@name: demo.py
@author: getTomsKnowledge
@date: 09/29/2024
@description: A vanilla program w/ no reusability or portability run straight through Python.

Taken from: https://www.youtube.com/watch?v=LWc-9v8RVwM (Algovibes, 09/28/2024)

"""

# Dependencies:
#import os
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Globals:
yearTrading = 252

"""
# Getting user's stock choice:
print(f"Hello, {os.environ.get()}!  Let's get started...")
"""

yesNoCont = "n"

while( yesNoCont == "n" ):
  tckrSym = input(f"Please input a ticker symbol:")
  yesNoCont = input(f"You entered {tckrSym}.  Is this correct? [y/n]")
end

# Get data:
df = yf.download(tckrSym)

# Normalize:
returns = np.log(1 + df['Adj Close']pct_change())

# Get normal distribution parameters:
mu, sigma = returns.mean(), returns.std()

# Get initial price for de-normalization ($):
price_init = df['Adj Close'].iloc[-1]

# Plug n' chug, plot outcome:
for i in range(100):
  sim_rets = np.random.normal(mu, sigma, yearTrading)
  sim_prices = price_init * (sim_rets + 1).cumprod()
  plt.axhline(price_init, c = 'k')
  plt.plot(sim_prices)

