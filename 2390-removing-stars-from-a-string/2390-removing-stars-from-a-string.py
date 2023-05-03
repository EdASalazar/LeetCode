class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if stack and s[i] == '*':
                stack.pop(-1)
            else: stack.append(s[i])

        return "".join(stack)