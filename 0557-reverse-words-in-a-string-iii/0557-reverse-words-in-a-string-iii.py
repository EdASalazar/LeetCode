class Solution:
    def reverseWords(self, s: str) -> str:
        newArr = s.split()

        # print(newArr[0][::-1])
        for i in range(0, len(newArr)):
            newArr[i] = newArr[i][::-1] 
    
        return " ".join(newArr)