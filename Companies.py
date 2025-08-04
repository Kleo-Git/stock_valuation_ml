from FinancialData import StockData
from valuation_methods import Valuation_Model
import pandas as pd


wiki_data = pd.read_html("https://en.wikipedia.org/wiki/List_of_S&P_500_companies")
sp500_companies = wiki_data[0]


companies = []

#Stick with small number for now, since full list takes way too long
#Look into optimizations later

#for i in range(10):
#    company_symbol = sp500_companies["Symbol"][i]
#    companies.append(StockData(company_symbol, "1y"))


apple = StockData("TSLA", "1y", 50, False)
stock_price = apple.get_latest_price()
apple_valuation = Valuation_Model(apple)

print(apple_valuation.pb_ratio_val())
print(apple_valuation.pe_ratio_val())


print(stock_price)


