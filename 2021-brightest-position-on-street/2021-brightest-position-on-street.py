class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        change = []
        for position, radius in lights:
            change.append([position - radius, 1])
            change.append([position + radius +1, -1])
        
        change.sort()
        print(change)
        ans = curr = brightest = 0
        for position, value in change:
            curr += value
            if curr > brightest:
                brightest = curr
                ans = position



        return ans