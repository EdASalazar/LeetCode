from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        counts = defaultdict(int)
        ans = []
        
        for num in nums:
            counts[num] += 1
        
        for key, value in counts.items():
            if value == 1:
                ans.append(key)
            
        if ans == []:
            return -1
        else:
            return max(ans)
            

