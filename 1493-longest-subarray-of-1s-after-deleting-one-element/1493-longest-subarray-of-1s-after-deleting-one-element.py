class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums: return 0
        if 0 not in nums: return len(nums) -1

        onesCounter = 0
        dummyCounter = 0
        zeroCounter = 0
        maxWindow = 0

        for num in nums:
            if num == 1:
                onesCounter += 1
            elif num == 0:
                dummyCounter, zeroCounter, onesCounter = onesCounter, 1, 0
            
            maxWindow = max(maxWindow, dummyCounter + onesCounter)


        return maxWindow if zeroCounter else (maxWindow - 1)