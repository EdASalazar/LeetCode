class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        pre = []
        total = 0
        
        
        for num in nums:
            total += num
            pre.append(total)
        print(pre)
  
        for i in range(len(queries)):
            j = len(pre) - 1
            print(j)
            while j >= 0:
                if pre[j] <= queries[i]:         
                    ans.append(j + 1)
                    print('1j', j)
                    break
                else:
                    j -= 1
                    if j < 0:
                        ans.append(0)
                    
        return ans     

                    