from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        curSum = 0
        prefixSums = { 0 : 1}
        
        for num in nums:
            curSum += num
            diff = curSum - goal

            ans += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return ans
