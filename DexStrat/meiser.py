from backtesting import Strategy
import pandas as pd

def VWAP(data):
    """
    Calculate the Volume-Weighted Average Price (VWAP).
    VWAP = Cumulative (Price * Volume) / Cumulative Volume
    """
    price_volume = data['Close'] * data['Volume']
    vwap = price_volume.cumsum() / data['Volume'].cumsum()
    return vwap

class VWAPStrategy(Strategy):
    def init(self):
        # Compute the VWAP
        self.vwap = self.I(VWAP, self.data)

    def next(self):
        # Buy signal: If the price is above the VWAP, buy
        if self.data.Close[-1] > self.vwap[-1]:
            if not self.position:  # Only buy if there's no existing position
                self.buy()
        
        # Sell signal: If the price is below the VWAP, sell
        elif self.data.Close[-1] < self.vwap[-1]:
            if self.position:  # Only sell if there's an existing position
                self.position.close()
