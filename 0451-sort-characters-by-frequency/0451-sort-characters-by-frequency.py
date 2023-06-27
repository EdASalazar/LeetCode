class Solution:
    def frequencySort(self, s: str) -> str:
        countLetters = collections.Counter(s)
        print(countLetters)
        newStr = ""
        sortedDict = sorted(countLetters.items(), key=lambda x:x[1], reverse=True)
        countLetters = dict(sortedDict)
        print(countLetters)

        for key, value in countLetters.items():
            counter = value
            while counter > 0:
                newStr += key
                counter -= 1

        return newStr