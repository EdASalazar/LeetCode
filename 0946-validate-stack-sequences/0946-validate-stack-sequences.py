class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ans = []
        i = 0

        for num in pushed:
            ans.append(num)

            while ans and ans[-1] == popped[i]:
                ans.pop()
                i += 1
        
        return len(ans) == 0

