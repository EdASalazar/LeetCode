class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        oneCounter = sorted(collections.Counter(word1).values())
        twoCounter = sorted(collections.Counter(word2).values())
        oneSet = set(x for x in word1)
        twoSet = set(x for x in word2)
        if oneCounter == twoCounter and oneSet == twoSet:
            return True


        return False

        