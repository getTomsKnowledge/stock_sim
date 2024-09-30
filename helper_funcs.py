"""
@Title: get_stock_data.py
@Author: getTomsKnowledge
@Date: 09/29/2024
@Description: gets stock info

"""

# Dependencies:

import yfinance as yf

yesNoCont = "n"

def get_stock_data(tckrSym):
  df = yf.download(tckrSym)
  returns = np.log(1 + df.