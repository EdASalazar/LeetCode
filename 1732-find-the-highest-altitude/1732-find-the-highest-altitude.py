class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0]
        total = 0
        
        for num in gain:
            total += num
            ans.append(total)
        
        return max(ans)
            