class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sqrArr = []
        sortArr = []
        i = 0
        
        while i < len(nums):
            sqrArr.append(nums[i] * nums[i])
            i += 1
        sqrArr.sort(reverse=False)
        return sqrArr
            
        
        