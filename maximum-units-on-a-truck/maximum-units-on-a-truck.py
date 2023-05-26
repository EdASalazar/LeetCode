import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x : x[1], reverse = True)
        ans = 0
        
        for box in boxTypes:
            inventory = box[0]
            while truckSize and inventory:
                ans += box[1]
                truckSize -= 1
                inventory -= 1
        
        return ans
            
        
         