class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = n - 1
        
        while i < j:
            dummy = s[i]
            dummyTwo = s[j]
            s[i] = dummyTwo
            s[j] = dummy
            i += 1
            j -= 1
     
        
        return s
        