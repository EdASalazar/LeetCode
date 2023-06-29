class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        mx, output = 0,0
        l = 0

        for i, n in enumerate(nums):
            if n in seen:
                while l < seen[n] + 1:
                    mx -= nums[l]
                    l += 1
            seen[n] = i
            mx +=n
            output = max(output, mx)
        
        return output

        