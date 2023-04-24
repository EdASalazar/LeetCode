from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_count = Counter(stones)
        ans = 0
        
        
        for jewel in jewels: 
            stone_item = stones_count[jewel]
            ans += stone_item

        return ans