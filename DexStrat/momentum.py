from backtesting import Strategy
import pandas as pd

def ROC(values, n):
    """
    Return the Rate of Change (ROC) of `values`, calculated
    as the percentage change from `n` periods ago.
    """
    return pd.Series(values).pct_change(periods=n) * 100

class MomentumStrategy(Strategy):
    # Define the momentum period as a class variable
    momentum_period = 5

    def init(self):
        # Precompute the rate of change (momentum)
        self.roc = self.I(ROC, self.data.Close, self.momentum_period)

    def next(self):
        # If momentum is greater than a threshold, buy the asset
        if self.roc[-1] > 1:  # Buy signal
            if not self.position:  # Only buy if there's no existing position
                self.buy()
        
        # If momentum is less than a negative threshold, sell the asset
        elif self.roc[-1] < -1:  # Sell signal
            if self.position:  # Only sell if there's an existing position
                self.position.close()
