class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = ans = 0
        
        for right in range(len(nums)):
            k -= 1 - nums[right]
            print(k)
            
            if k < 0:
                k += 1 - nums[left]
                left += 1

        
        return right - left +1
            