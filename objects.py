from itertools import product

class Stocks:

    @staticmethod
    def calc_max_interest(prices): 
        pairs = []  
        while len(prices) > 0:
            price = prices.pop(0)
            pairs = pairs + list(product([price], prices))
            
        return max(max([b-a for (a,b) in pairs]), 0)