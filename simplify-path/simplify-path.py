class Solution:
    def simplifyPath(self, path: str) -> str:
        stack =[]
        
        for el in path.split("/"): 
            if el == "..":
                if stack: 
                    stack.pop()

            elif el == "." or not el:
                continue 
            else: 
                stack.append(el)

        
        answer = "/" + "/".join(stack)
        return answer