from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
cg.ping()

import datetime
import time

def Unix_Time(year, month, day, hour, second):
    date_time = datetime.datetime(year,month,day,hour,second)
    return time.mktime(date_time.timetuple())

def Human_time(Unix_Time):
    return datetime.datetime.fromtimestamp(Unix_Time)

start_time = Unix_Time(2023,1,1,0,0)
end_time = Unix_Time(2023,2,1,0,0)
print(start_time)
print(end_time)

bitcoin_price = cg.get_coin_market_chart_range_by_id(
    id= 'bitcoin',
    vs_currency='usd',
    from_timestamp=start_time,
    to_timestamp=end_time

)
eth_price = cg.get_coin_market_chart_range_by_id(
    id= 'ethereum',
    vs_currency='usd',
    from_timestamp=start_time,
    to_timestamp=end_time

)
print('Keys:', bitcoin_price.keys())
price_table = pd.DataFrame(bitcoin_price)
print(price_table)
print("BTC Length", len(bitcoin_price['prices']))
print("Eth Length", len(eth_price['prices']))

btc={}
btc['time'] =[x[0]for x in bitcoin_price['prices']]
btc['price'] = [x[1] for x in bitcoin_price['prices']]


eth={}
eth['time'] = [x[0] for x in eth_price['prices']]
eth['price'] = [x[1] for x in eth_price['prices']]

import seaborn as sbn
import matplotlib.pyplot as ml

sbn.set(rc = {'figure.figsize': (13,9)})
sbn.set_theme(style= "darkgrid")

sbn.lineplot(
    x ='time',
    y = 'price',
    data = btc
)

ax2 = ml.twinx()

sbn.lineplot(
    x='time',
    y = 'price',
    data = eth,
    ax = ax2,
    color = 'r'
    )

ml.show()

