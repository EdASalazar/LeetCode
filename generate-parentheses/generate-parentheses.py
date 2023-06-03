class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(curr_string, left_counter, right_counter):
            if len(curr_string) == 2 * n:
                answer.append(''.join(curr_string))
                return

            if left_counter < n:
                curr_string.append('(')
                print(curr_string)
                backtrack(curr_string, left_counter + 1, right_counter)
                curr_string.pop()
                
            if right_counter < left_counter:
                curr_string.append(')')
                print(curr_string)
                backtrack(curr_string, left_counter, right_counter + 1)
                curr_string.pop()

            
            

            
    
        backtrack([], 0, 0)
        return answer
        