
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dictNums = collections.Counter(nums)
        ans = 0

        for key, val in dictNums.items():
            if val == 1:
                ans += key


        return ans