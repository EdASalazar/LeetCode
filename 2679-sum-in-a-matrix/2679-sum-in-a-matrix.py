class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = 0
        nums = [sorted(num) for num in nums]

        while any(nums):
            temp = 0
            for num in nums:
                temp = max(temp, num.pop())
            ans += temp 
        

               
        return ans