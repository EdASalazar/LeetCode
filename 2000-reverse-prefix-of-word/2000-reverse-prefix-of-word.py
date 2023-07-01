class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        chIdx = word.index(ch)
        newStr =""
        
        newStr = word[:chIdx+1][::-1] + word[chIdx+1:]
        
        return newStr 