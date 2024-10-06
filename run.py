from backtesting import Backtest
from DexStrat.momentum import MomentumStrategy
from DexStrat.random import RandomTradeStrategy
from LincolnStrat.strat import SmaCross
from backtesting.test import GOOG

# bt = Backtest(GOOG, SmaCross, cash=10_000, commission=.002)
# stats = bt.run()
# print(stats)

# bt_momentum = Backtest(GOOG, MomentumStrategy, cash=10_000, commission=.002)
# stats_momentum = bt_momentum.run()
# print(stats_momentum)

# bt_random = Backtest(GOOG, RandomTradeStrategy, cash=10_000, commission=.002)
# stats_random = bt_random.run()
# print(stats_random)