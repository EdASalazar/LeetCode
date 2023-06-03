class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        
        
        def backtrack(digit):
            if len(digit) == n:
                print('backtrack')
                num = (int(''.join(map(str, digit))))
                str(num)
                if len(str(num)) == n:
                    ans.append(num)
                return
            
            for i in range(0, 10):
                if digit == []:
                    print('if 1')
                    digit.append(i)
                    print('if 1', digit)
                    backtrack(digit)
                    digit.pop()
                else:
                    if abs(i - digit[-1]) == k:
                        print('if 2')
                        digit.append(i)
                        print('if 2', digit)
                        backtrack(digit)
                        digit.pop()
                        
        ans = []
        backtrack([])
        return ans
                
                