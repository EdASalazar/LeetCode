class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.append(s[i])
            elif stack and stack[-1].upper() == s[i]:
                stack.pop()
                i = 0
            elif stack and stack[-1] == s[i].upper():
                stack.pop()
                i = 0
            else: 
                stack.append(s[i])
        # s = "".join(stack)    
        
        print(stack)
        return "".join(stack)