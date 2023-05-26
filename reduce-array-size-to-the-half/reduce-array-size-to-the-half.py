from collections import Counter
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        target = len(arr) // 2 + len(arr) % 2
        numsDict = Counter(arr)
        ans = 0

        numsDict = [-value for value in numsDict.values()]
        heapq.heapify(numsDict)

        while target > 0:
            target += heapq.heappop(numsDict)
            ans +=1
        
        return ans

            