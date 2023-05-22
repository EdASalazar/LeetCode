from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = Counter(nums)
        heap = heapq.nlargest(k, numsDict.keys(), key=numsDict.get)





        return heap