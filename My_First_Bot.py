# Import the libraries
from poloniex import Poloniex
import pandas as pd
import time
import os

#Public API
# polo = Poloniex()
# ticker = polo.returnTicker()['BTC_ETH']
# print(ticker)

#Private API
# api_key = os.environ.get('POLONIEX_API_KEY')
# api_secret = os.environ.get('POLONIEX_SECRET')
# polo = Poloniex(api_key, api_secret)

api_key = os.environ.get('IRE89ZGW-OWJ4PP7M-PNQMXRKD-YHDKAZHZ')
api_secret = os.environ.get('df136bbf858f31a245f4afd2ce051b5bf4742d54ab4580e26f9e10069e09685bd95948e9a77f72a653b037bafc78ede53673cf6f1ca898e25de6a3416dbb4fe6')
polo = Poloniex(api_key, api_secret)

ticker = polo.returnTicker()['BTC_ETH']
print(ticker)

# balances = polo.returnBalances()
# print(balances)