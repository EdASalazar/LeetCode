from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = []
        
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))
            
        
        print(heap)
        return [heappop(heap)[1] for _ in range(k) ]
            
        