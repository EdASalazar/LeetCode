class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # num_set = set(nums)
        # n = len(nums) +1

        # for number in range(n):
        #     if number not in num_set:
        #         return number


        missing = len(nums)
        for i,  num in enumerate(nums):
            missing ^= i ^ num
        return missing