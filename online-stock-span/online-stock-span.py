from collections import deque

class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
            
        self.stack.append([price, ans])
        
        print(self.stack)
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)