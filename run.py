from backtesting import Backtest
from LincolnStrat.smaStrat import SmaCross
from backtesting.test import GOOG, EURUSD
import yfinance as yf

tick = yf.Ticker("ZIM")
historical_data = tick.history(start="2024-8-7", end="2024-9-7")
#dataF = yf.download("EURUSD", start="2024-8-7", end="2023-9-7", interval='15m')
print(type(GOOG))
print(type(historical_data))

bt = Backtest(historical_data, SmaCross, cash=10_000, commission=.002)
stats = bt.run()
print(stats)
