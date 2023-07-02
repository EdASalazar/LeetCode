class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        characterDict = {}
        wordDict = {}
        words = s.split()
        
        if len(words) != len(pattern):
            return False

        for char, word in zip(pattern, words):
            if char not in characterDict:
                if word in wordDict:
                    return False
                else:
                    characterDict[char] = word
                    wordDict[word] = char
            else:
                if characterDict[char] != word:
                    return False

        
        return True 