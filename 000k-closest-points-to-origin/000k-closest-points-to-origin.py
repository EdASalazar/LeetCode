from collections import defaultdict
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points: 
            heapq.heappush(heap, ((point[0]**2 + point[1]**2), (point[0], point[1])))
         
        
        
        return [heappop(heap)[1] for _ in range(k)]
        
        
        
        