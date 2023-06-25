class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityDict = dict(paths)
        print(cityDict)

        for i in cityDict.values():
            if i not in cityDict.keys():
                return i