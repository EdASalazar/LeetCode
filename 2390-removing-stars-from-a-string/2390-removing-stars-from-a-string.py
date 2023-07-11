from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        ans = []

        for el in s:
            if el == '*':
                ans.pop()
            else:
                ans += [el]
   
        return ''.join(ans)
        