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
    #Intialize company with relevant data
    def __init__(self, company_name, duration="1y", show_plot=False):
        self.company_name = company_name
        self.duration = duration
        self.ticker = yf.Ticker(company_name)
        self.price_data = self.ticker.history(duration)
        #Auto run fetch fundamentals
        self.fundamentals = self.fetch_fundamentals()
        #Only show plot if wanted
        if show_plot:
            self.plot_stock_price()
    
    #Function to plot stock price over duration
    def plot_stock_price(self):
        #Creates plot based on data from close prices
        self.price_data["Close"].plot(title =  self.company_name + " Stock Price")
        plt.show()
    
    def fetch_fundamentals(self):
        #List of fundamental data created manually for now
        #Currently list is fairly arbitrary, although all this data is useful
        fundamental_data = ["trailingPE", "forwardPE", "trailingPegRatio", "priceToBook", "dividendYield"
        , "trailingEps", "forwardEps", "revenueGrowth", "debtToEquity", "returnOnEquity",
        "profitMargins"]
        
        company_fundamentals = []
        #Find each type of fundamental data from above list
        for dataType in fundamental_data:
            company_fundamentals.append(self.ticker.info.get(dataType, np.nan))
        
        #Return in a dictionary, and zipped for simple understanding and data manipulation
        return dict(zip(fundamental_data, company_fundamentals))
    
    #Return the fundamental data
    def get_fundamentals(self):
        return self.fundamentals
    
apple = StockData("AAPL")

print(apple.get_fundamentals())


    
    