import random
from backtesting import Strategy

class RandomTradeStrategy(Strategy):
    # Define parameters
    trade_probability = 0.5  # Probability to make a trade in a given step

    def init(self):
        pass  # No initialization needed for random trading

    def next(self):
        # Randomly decide to buy or sell based on the trade probability
        if random.random() < self.trade_probability:
            # Randomly choose to buy or sell
            if not self.position.is_long and not self.position.is_short:
                # Randomly choose to buy or sell
                if random.choice([True, False]):
                    self.buy()
                else:
                    self.sell()
            elif self.position.is_long:
                # Randomly close the long position or do nothing
                if random.random() < self.trade_probability:
                    self.position.close()
            elif self.position.is_short:
                # Randomly close the short position or do nothing
                if random.random() < self.trade_probability:
                    self.position.close()
