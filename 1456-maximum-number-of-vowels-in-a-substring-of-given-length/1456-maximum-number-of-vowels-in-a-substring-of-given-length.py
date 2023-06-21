class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowles = ['a', 'e', 'i', 'o', 'u']
        maxVowles = 0
        i = j = 0
        curr = 0

        for j in range(len(s)):
            if s[j] in vowles:
                print(s[j])
                curr += 1
                maxVowles = max(curr, maxVowles)
                print(curr, maxVowles)

            if j - i +1 == k:
                if s[i] in vowles:
                    curr -= 1
                    print(curr, maxVowles)
                i += 1


        return maxVowles if maxVowles != float('-inf') else 0