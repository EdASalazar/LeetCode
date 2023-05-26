class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        k = 5000
        ans = 0
        
        for x in weight:
            if x <= k:
                k -= x
                ans +=1
        
        return ans