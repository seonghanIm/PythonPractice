
import ccxt
from datetime import datetime

binance = ccxt.binance()
ohlcvs = binance.fetch_ohlcv('ETH/BTC') ##수정 가능 1d, 1m, 1M
while True:
    for ohlc in ohlcvs:
        print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), " open:",ohlc[1],"    high:",ohlc[2],"low:",ohlc[3],"Volume:",ohlc[4]) #과거 데이터 조회