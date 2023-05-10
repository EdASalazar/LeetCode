class Solution:
    def reverseWords(self, s: str) -> str:
        newArr = s.split()
        ans = []

        # print(newArr[0][::-1])
        for i in range(0, len(newArr)):
            reversedWord = newArr[i][::-1]
            ans.append(reversedWord) 
    
        return " ".join(ans)