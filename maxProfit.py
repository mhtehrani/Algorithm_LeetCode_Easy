"""
Maximize Profit in Stock Trading
================================

@author: mhtehrani
November 05, 2021
https://github.com/mhtehrani

"""

def maxProfit(prices):
    buy = prices[0]
    sell = prices[0]
    profit = sell - buy
    for i in range(0,len(prices)):
        if prices[i] <= buy:
            buy = prices[i]
            sell = prices[i]
        elif prices[i] > sell:
            sell = prices[i]
        #end
        if sell - buy > profit:
            profit = sell - buy
        #end
    #end
    
    return profit
#end

prices = [2,4,1]
print(maxProfit(prices))


