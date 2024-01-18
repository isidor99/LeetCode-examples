class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # save day when stock was cheapest
        m = 0
        
        # save maximum profit
        max_profit = 0
        
        for i in range(1, len(prices)):
            
            # find difference between price on i-th day and day when stock was cheapest
            d = prices[i] - prices[m]
            
            # if difference is bigger then maximum profit, then we have new maximum profit
            if d > max_profit:
                max_profit = d
            
            # if price on i-th day is less than price of previous cheapest stock, save new day
            if prices[i] < prices[m]:
                m = i

        # return result
        return max_profit