from backtesting import Backtest
from DexStrat.momentum import MomentumStrategy
from DexStrat.random import RandomTradeStrategy
from DexStrat.BollingerRSIStrategy import BollingerRSIStrategy
from DexStrat.meiser import VWAPStrategy
from LincolnStrat.strat import SmaCross
import yfinance as yf
import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
import pandas as pd

# Function to run the backtest
def run_backtest(strategy_class, output_box, start_date, end_date, ticker): 
    # Clear the output box
    output_box.delete(1.0, tk.END)

    # Convert start and end dates to datetime format
    try:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
    except ValueError:
        output_box.insert(tk.END, "Invalid date format. Please use YYYY-MM-DD.\n")
        return

    # Fetch the stock data using yfinance
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
    except Exception as e:
        output_box.insert(tk.END, f"Error fetching data: {e}\n")
        return

    # Check if data is empty
    if stock_data.empty:
        output_box.insert(tk.END, "No data available for the selected ticker and date range.\n")
        return

    # Run the backtest for the selected strategy
    bt = Backtest(stock_data, strategy_class, cash=10_000, commission=.002)
    stats = bt.run()

    # Output the results in the text box
    output_box.insert(tk.END, f"Backtest Results:\n{stats}")

# Main application window
class BacktestApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Backtest Strategies")
        self.geometry("600x600")

        # Load the background image
        self.bg_image = Image.open(r"C:\Users\666ba\Documents\Coding projects\owlhacks 2024\algoTrader\ui.jpg")
        self.bg_image = self.bg_image.resize((600, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a label to hold the background image
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Dropdown to select strategy
        ttk.Label(self, text="Select a Strategy:").pack(pady=10)
        self.strategy_var = tk.StringVar()
        strategy_choices = ['SmaCross', 'MomentumStrategy', 'RandomTradeStrategy', 'BollingerRSIStrategy', 'VWAPStrategy']
        strategy_menu = ttk.Combobox(self, textvariable=self.strategy_var, values=strategy_choices)
        strategy_menu.pack(pady=10)

        # Entry field for stock ticker
        ttk.Label(self, text="Stock Ticker:").pack(pady=5)
        self.ticker_var = tk.StringVar()  # Variable to hold the ticker
        ticker_entry = ttk.Entry(self, textvariable=self.ticker_var)
        ticker_entry.pack(pady=5)

        # Entry fields for start and end date
        ttk.Label(self, text="Start Date (YYYY-MM-DD):").pack(pady=5)
        self.start_date_var = tk.StringVar(value="2004-08-19")  # Default start date
        start_date_entry = ttk.Entry(self, textvariable=self.start_date_var)
        start_date_entry.pack(pady=5)

        ttk.Label(self, text="End Date (YYYY-MM-DD):").pack(pady=5)
        self.end_date_var = tk.StringVar(value="2013-03-01")  # Default end date
        end_date_entry = ttk.Entry(self, textvariable=self.end_date_var)
        end_date_entry.pack(pady=5)

        # Button to run backtest
        run_button = ttk.Button(self, text="Run Backtest", command=self.run_selected_strategy)
        run_button.pack(pady=10)

        # Output box to display results
        self.output_box = scrolledtext.ScrolledText(self, width=70, height=15)
        self.output_box.pack(pady=20)

    # Function to determine which strategy was selected and run it
    def run_selected_strategy(self):
        strategy_name = self.strategy_var.get()
        start_date = self.start_date_var.get()
        end_date = self.end_date_var.get()
        ticker = self.ticker_var.get()  # Get the ticker from the input

        # Map strategy names to actual classes
        strategies = {
            'SmaCross': SmaCross,
            'MomentumStrategy': MomentumStrategy,
            'RandomTradeStrategy': RandomTradeStrategy,
            'BollingerRSIStrategy': BollingerRSIStrategy,
            'VWAPStrategy': VWAPStrategy
        }

        # Run the backtest with the selected strategy and display the output
        if strategy_name in strategies:
            run_backtest(strategies[strategy_name], self.output_box, start_date, end_date, ticker)
        else:
            self.output_box.insert(tk.END, "Please select a valid strategy.\n")

# Main program execution
if __name__ == "__main__":
    app = BacktestApp()
    app.mainloop()
