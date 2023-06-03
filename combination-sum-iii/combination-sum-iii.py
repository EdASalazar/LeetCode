class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(numbers, start):
            if sum(numbers) == n and len(numbers) == k:
                ans.append(list(numbers))
                return
            elif len(numbers) == k and sum(numbers) != n:
                return  
         
            
            for i in range(start, 10):
                numbers.append(i)            
                backtrack(numbers, i + 1)
                numbers.pop()
            


        ans = []
        backtrack([], 1)
   
        return ans