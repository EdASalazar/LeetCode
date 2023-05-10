class Solution:
    def reverseWords(self, s: str) -> str:
        newArr = s.split()
        ans = []

        # print(newArr[0][::-1])
        for i in range(0, len(newArr)):
            ans.append(newArr[i][::-1]) 
    
        return " ".join(ans)