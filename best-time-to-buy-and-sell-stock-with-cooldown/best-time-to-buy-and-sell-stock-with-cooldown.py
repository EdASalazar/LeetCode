class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0
        hold, free = [float('-inf')] * n, [0] * n
        

        for i in range(n):
            free[i] = max(free[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], free[i - 2] - prices[i])
            
        
        
        return free[-1]
        
        
        
        