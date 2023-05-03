class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums1)):
            for j in range(0, len(nums2)):
                pointer, curr = 1, 0
                
                if nums1[i] == nums2[j]:
                    curr = nums2[j]
                    
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > curr:
                            ans.append(nums2[k])
                            pointer = 0
                            break
                
                    if pointer == 1:
                        print(ans)
                        ans.append(-1)
                
            
          
        
        return ans