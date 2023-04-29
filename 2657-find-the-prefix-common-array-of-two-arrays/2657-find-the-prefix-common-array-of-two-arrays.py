class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # feels a single pointer. 
        # can I do this without a ton of if statments.
        ans = []
        curr = 0
        curr_range = 1
        
        while len(A) > curr_range -1:
            for i in range(0, curr_range):
                for j in range(0, curr_range):
                    if A[i] == B[j]:
                        curr += 1
            
            print(curr_range)
            ans.append(curr)
            curr = 0
            curr_range += 1

        return ans