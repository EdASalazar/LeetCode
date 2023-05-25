from collections import defaultdict
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points: 
            pointOne = point[0]
            pointTwo = point[1]
            distance = pointOne**2 + pointTwo**2
            print(pointOne, pointTwo, distance)
            heapq.heappush(heap, (distance, (pointOne, pointTwo)))
         
        
        print(heap)
        
        return [heappop(heap)[1] for _ in range(k)]
        
        
        
        