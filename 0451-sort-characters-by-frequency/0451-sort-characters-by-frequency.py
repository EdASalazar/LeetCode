class Solution:
    def frequencySort(self, s: str) -> str:
        countLetters = collections.Counter(s)
        newStr = ""
        
        for letter, value in countLetters.most_common():
            newStr += letter * value

        return newStr