import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        
        while k > 0:
            num = heapq.heappop(piles)
            heapq.heappush(piles, num // 2)

            k -= 1
            
        
        return sum(piles) * -1
        