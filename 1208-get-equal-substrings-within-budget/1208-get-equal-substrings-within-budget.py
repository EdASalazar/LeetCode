class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        totalCost = 0
        maxLen = 0
        i = 0
 

        for j in range(len(s)):
            totalCost += abs(ord(s[j]) - ord(t[j]))
            if totalCost <= maxCost:
                maxLen = max(maxLen, j - i + 1)
            else: 
                maxLen = max(maxLen, j - i)
                totalCost -= abs(ord(s[i]) - ord(t[i]))
                i += 1

   
        return maxLen