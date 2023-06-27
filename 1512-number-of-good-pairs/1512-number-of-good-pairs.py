class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        hashMap = {}

        for num in nums:
            if num in hashMap:
                ans += hashMap[num]
                hashMap[num] += 1
            else:
                hashMap[num] = 1
  
        return ans
