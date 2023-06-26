class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dict = {}
        currentIndex = (0,0)

        for i in path:
            dict[(0, 0)] = 1
            if i == 'N':
                currentIndex = (currentIndex[0] + 1, currentIndex[1])
            elif i == 'S':
                currentIndex = (currentIndex[0] -1, currentIndex[1])
            elif i == 'E':
                currentIndex = (currentIndex[0], currentIndex[1] + 1)
            else:
                currentIndex = (currentIndex[0], currentIndex[1] -1)

            if currentIndex in dict.keys():
                return True
            else:
                dict[currentIndex] = 1
             
        return False       
                
