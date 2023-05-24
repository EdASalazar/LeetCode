import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0

        while len(sticks) > 1:
            numOne = heapq.heappop(sticks)
            numTwo = heapq.heappop(sticks)
            cost += numOne + numTwo
            heapq.heappush(sticks, (numOne + numTwo))
            # print(numOne, numTwo, cost, sticks)
            
        return cost    