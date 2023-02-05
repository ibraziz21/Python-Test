#trying out coingecko API
import pandas as pd
import datetime as dt
import time as t
import plotly.graph_objects as go
from plotly import offline
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
print(cg.ping())

# get coin list
coinlist = cg.get_coins_list()
coinDataFrame = pd.DataFrame.from_dict(coinlist)
print(coinDataFrame)

supported = cg.get_supported_vs_currencies()
print(supported)
coins =['bitcoin', 'ethereum']

complexRequest = cg.get_price(ids = coins,
                vs_currencies='usd',
                include_market_cap = True )

print(complexRequest)

#asset platforms  (chains)
chains = cg.get_asset_platforms()
DataChain = pd.DataFrame.from_dict(chains)
print(DataChain)