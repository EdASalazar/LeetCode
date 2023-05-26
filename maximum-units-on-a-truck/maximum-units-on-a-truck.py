import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        def sortSecond(val):
            return val[1]
        k = truckSize
        boxTypes.sort(key=sortSecond, reverse=True)
        print(boxTypes)
        ans = 0
        
        for box in boxTypes:
            inventory = box[0]
            while k and inventory:
                ans += box[1]
                k -= 1
                inventory -= 1
        
        return ans
            
        
         