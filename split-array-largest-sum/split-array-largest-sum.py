class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        if k == 1:
            return right
        
        if k == len(nums):
            return max(nums)
        
        while left < right:
            mid = (left + right) // 2

            total = 0
            splits = 1
            for num in nums:
                total += num
                if total > mid:
                    total = num
                    splits += 1
                
            if splits > k:
                left = mid + 1
            else:
                right = mid 
              
        return right
            
        