from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: 
            return []

        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }
        

        def backtrack(index, path):
            if len(path) == len(digits):
                combos.append(''.join(path))
                return
        
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                print('first', index, path)
                backtrack(index + 1, path)
                print('back', index, path)
                path.pop()
                print('pop',index, path )

                
        combos = []   
        backtrack(0, [])  
        return combos
            