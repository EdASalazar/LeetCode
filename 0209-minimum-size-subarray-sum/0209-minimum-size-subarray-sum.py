class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1

        i = j = 0
        total = 0
        minLen = float('inf')

        for j in range(len(nums)):
            total += nums[j]

            while total >= target:
                minLen = min(minLen, j - i +1)
                total -= nums[i]
                i += 1
            
        
        return minLen if minLen != float('inf') else 0






