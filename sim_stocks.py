"""
@title: sim_stocks.py
@author: getTomsKnowledge
@date: 09/29/2024
@description: 

"""

# Dependencies:
import os
import numpy as np
import matplotlib.pyplot as plt
from helper_funcs import get_stock_data

# Getting started:
yearTrading = 252
userName = os.environ.get('USER')

# Greet the user
print(f"Hello, {userName}, it's good to see you!")

# Get ticker symbol

while(yesNoCont == "n"):
  tckrSym = input("Please enter a ticker symbol:")
  yesNoCont = input(f"You chose, {tckrSym}. Is this correct? [y/n]"
end

print(f"Generating sim for {tckrSym}...")
get_stock_data(tckrSym)
