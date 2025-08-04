import numpy as np

#Look into caching .get_fundamentals so dont have to call multiple times

class Valuation_Model:
    def __init__(self, company):
        self.company_data = company
        self.fundamentals = self.company_data.get_fundamentals()
        
    #Function to evaluate intrinsic price based on P/E ratio
    def pe_ratio_val(self):
        
        trailing_eps = self.fundamentals.get("forwardEps")
        
        pe_ratio = self.fundamentals.get("forwardPE")
        
        #Simple price calculation
        price = trailing_eps*pe_ratio
        
        return(price)
    
    #Function to evaluate intrinsic price based on P/B ratio
    def pb_ratio_val(self):
        
        book_value_per_share = self.fundamentals.get("bookValue")
        
        pb_ratio = self.fundamentals.get("priceToBook")
        
        price = book_value_per_share * pb_ratio
        
        return(price)
    
    #Function to evaluate intrinsic price based dividend discount model
    #Only applicable to companies with dividends
    def ddm_val(self, expected_div, req_return, div_growth_rate):
        
        price = expected_div / (req_return - div_growth_rate)
        
        return(price)
    
    def fcf_val(self, op_cash_flow, cap_exp):
        
        fcf_value = op_cash_flow - cap_exp
        
        return(fcf_value)
    
    def dcf_val(self, fcf_list, discount_rate, terminal_growth_rate):
        
        n = len(fcf_list)
        
        terminal_value = fcf_list[-1] * (1+terminal_growth_rate) / (discount_rate - terminal_growth_rate)
        
        discounted_TV = terminal_value / (1 + discount_rate)**n
        
        dcf_price = 0
        
        for t in range(n):
            dcf_price += fcf_list[t] / (1 + discount_rate)**t
            
        dcf_price += discounted_TV
        
        return(dcf_price)
    
    #Additional methods to look into:
    #RIM, EPV, SOTP
    
    
    
    