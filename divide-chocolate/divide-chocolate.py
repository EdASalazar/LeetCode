class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
  


        people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // people

        if len(sweetness) < people:
            return 1
  
        while left < right:
            mid = (left + right + 1) // 2
            curr = 0
            chunks = 0
            for s in sweetness:
                curr += s
                if curr >= mid:
                    chunks += 1
                    curr = 0
            if chunks >= people:
                left = mid
            else:
                right = mid - 1

        
        return right