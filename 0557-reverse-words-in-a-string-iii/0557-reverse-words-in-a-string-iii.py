class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ans = ""
        print(words)
        for word in words:
            ans += "".join(word[:: -1]) + " "
        ans = ans.rstrip()



        print(ans)
        return ans
        