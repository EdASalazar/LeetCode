class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]: 
        
        def backtrack(digit):
            if len(digit) == n:
                num = (int(''.join(map(str, digit))))
                if len(str(num)) == n:
                    ans.append(num)
                return
            
            for i in range(10):
                if digit == []:
                    digit.append(i)
                    backtrack(digit)
                    digit.pop()
                else:
                    if abs(i - digit[-1]) == k:
                        digit.append(i)                   
                        backtrack(digit)
                        digit.pop()
                        
        ans = []
        backtrack([])
        return ans
                
                