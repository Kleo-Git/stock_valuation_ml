import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

#Currently focusing on fundamentals for prediction
#Could also use price features, moving 10,50,100 day averages, RSI, MACD, Bollinger Bands/
#Daily % Returns, Volatility.

#Also could look at general economy (seems much more difficult to account for, esp different regions)
#Federal funds, inflation, GDP growth, unemployment etc.

#Company fundamentals semi-arbitrarily chosen to be used currently:
#P/E, PEG, P/B, Dividend Yield, EPS, Revenue growth, Debt to equity, Return on equity /
#Free cash flow, Net income margin.

class StockData:
    def __init__(self, company_name, duration="1y", show_plot=False):
        self.company_name = company_name
        self.duration = duration
        self.ticker = yf.Ticker(company_name)
        self.price_data = self.ticker.history(duration)
        self.fundamentals = self.fetch_fundamentals()
        if show_plot:
            self.plot_stock_price()
    
    def plot_stock_price(self):
        self.price_data["Close"].plot(title =  self.company_name + " Stock Price")
        plt.show()
    
    def fetch_fundamentals(self):
        fundamental_data = ["trailingPE", "forwardPE", "trailingPegRatio", "priceToBook", "dividendYield"
        , "trailingEps", "forwardEps", "revenueGrowth", "debtToEquity", "returnOnEquity",
        "profitMargins"]
        
        company_fundamentals = []
        
        for dataType in fundamental_data:
            company_fundamentals.append(self.ticker.info.get(dataType, np.nan))
            
        return dict(zip(fundamental_data, company_fundamentals))
    
    def get_fundamentals(self):
        return self.fundamentals
    
apple = StockData("AAPL")

print(apple.get_fundamentals())


    
    