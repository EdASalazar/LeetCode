class Solution:
    def maximum69Number (self, num: int) -> int:
        numbers = [int(x) for x in str(num)]
        print(numbers)
        
        for i in range(len(numbers)):
            if numbers[i] == 6:
                numbers[i] = 9
                break
               
        s = [str(num) for num in numbers]
        a_string = ''.join(s)
        return int(a_string)
    
