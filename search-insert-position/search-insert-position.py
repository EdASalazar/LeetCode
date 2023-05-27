class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        print(left, right)
        
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            print(num)
        
            if num == target:
                return nums.index(num)

            if num > target:
                right = mid - 1
            else:
                left = mid + 1

        
        return left 