from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # similar to the gene question
        # need to validate after we get the new index
        currVal = arr[start]
        seen = set()
        seen.add(start)
        index = start
        queue = deque([start])
    
        while queue:
            index = queue.popleft()
            currVal = arr[index]
            
            if currVal == 0:
                return True
            
            for change in [-currVal, currVal]:
                nextIndex = index + change
                if 0 <= nextIndex < len(arr) and nextIndex not in seen:
                    seen.add(nextIndex)
                    queue.append(nextIndex)

        return False
                    
                
                
            
        
        
        
        