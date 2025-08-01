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

        
def company_fundamental_data(company_name, time_duration, show_plot=False):
    #Accessing data from yfinance
    ticker = yf.Ticker(company_name)
    #Finding the stock price over given time period
    company_data = ticker.history(time_duration)
    
    #Finding all company fundamentals and returning in form of an array
    
    #For now manual input of desired types of fundamental data
    fundamental_data = ["trailingPE", "forwardPE", "trailingPegRatio", "priceToBook", "dividendYield"
    , "trailingEps", "forwardEps", "revenueGrowth", "debtToEquity", "returnOnEquity",
    "profitMargins"]
    #Empty list to store data
    company_fundamentals = []
    for dataType in fundamental_data:
        company_fundamentals.append(ticker.info.get(dataType, np.nan))
    
    #Can show plot for pricing if desired
    if show_plot:
        company_data["Close"].plot(title =  company_name + " Stock Price")
        plt.show()
        
    return dict(zip(fundamental_data, company_fundamentals))
        
    
print(company_fundamental_data("AAPL", "1y"))


    
    