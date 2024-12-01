class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        (INPUTS):
            prices: List[int]
            Description: "An array of prices of a given stock"
                         "The indicies represent the day of the price"
        (OUTPUTS):
            profit: int
            Description: "The maximum profit you can achieve from a transaction"
                         "Return 0 if you cannot achieve any profit"
        
        (PROBLEM DESCRIPTION):
            Buy a stock on a single day
            Sell that stock on another day to maximize the profit
        
        (EXAMPLE):
            INPUTS: List[int] = [9, 7, 3, 10, 1]
            OUTPUTS: int = 7
        (ASSUMPTIONS and CONSTRAINTS):
            1. You cannot buy sell on a previous day while buying on the day
               afterwards.
            2. You cannot have an empty array
            3. The prices are bigger than or equal to 1
        """
        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] > min_price:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit
        """
        [9, 7, 3, 10, 1]
        i   prices[i]   min_price   profit  max_profit
        0       9           [9]                 0
        1       7           9->[7]              0
        2       3           7->[3]              0
        3       10          [3]         7       0->[7]
        4       1           [1]                 [7]
        """
        return max_profit # 7