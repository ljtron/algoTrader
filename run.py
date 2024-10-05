from backtesting import Backtest
from LincolnStrat.strat import SmaCross
from backtesting.test import GOOG

bt = Backtest(GOOG, SmaCross, cash=10_000, commission=.002)
stats = bt.run()
print(stats)