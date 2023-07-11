from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        strQueue = deque(s)
        ans = ""
      

        while strQueue: 
            curr = strQueue.popleft()
            if curr == "*" and ans:
                ans = ans[:len(ans)-1]
            else:
                ans += curr
   
        return ans
        