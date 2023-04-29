class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        test = 0
        ans = 0
        nums.sort()
        
        while test < k:
            ans += nums[-1]
            nums[-1] += 1
            test +=1
            
        return ans