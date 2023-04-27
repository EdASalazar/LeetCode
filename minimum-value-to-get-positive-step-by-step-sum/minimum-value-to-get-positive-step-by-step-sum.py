class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        start_value = 1
        
        for num in nums: 
            prefix += num
            start_value = max(start_value, 1-prefix)
            
        return start_value

            