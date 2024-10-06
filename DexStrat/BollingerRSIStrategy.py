from backtesting import Strategy
import pandas as pd

def RSI(values, n):
    """
    Return the Relative Strength Index (RSI) of `values`.
    """
    delta = pd.Series(values).diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=n).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=n).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def BollingerBands(values, n, k):
    """
    Return the upper and lower Bollinger Bands.
    """
    sma = pd.Series(values).rolling(window=n).mean()
    std = pd.Series(values).rolling(window=n).std()
    upper_band = sma + (std * k)
    lower_band = sma - (std * k)
    return upper_band, lower_band

class BollingerRSIStrategy(Strategy):
    # Define parameters for the strategy
    rsi_period = 14
    bb_period = 20
    bb_std_dev = 2
    rsi_overbought = 70
    rsi_oversold = 30

    def init(self):
        # Compute the Bollinger Bands and RSI
        self.upper_band, self.lower_band = self.I(BollingerBands, self.data.Close, self.bb_period, self.bb_std_dev)
        self.rsi = self.I(RSI, self.data.Close, self.rsi_period)

    def next(self):
        # Buy signal: price touches lower Bollinger Band and RSI is below oversold level
        if self.data.Close[-1] < self.lower_band[-1] and self.rsi[-1] < self.rsi_oversold:
            if not self.position:  # Only buy if there's no existing position
                self.buy()

        # Sell signal: price touches upper Bollinger Band and RSI is above overbought level
        elif self.data.Close[-1] > self.upper_band[-1] and self.rsi[-1] > self.rsi_overbought:
            if self.position:  # Only sell if there's an existing position
                self.position.close()
