class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        ans = 0
        
        for x in arr:
            if x + 1 in hash_set:
                ans += 1
        return ans
            