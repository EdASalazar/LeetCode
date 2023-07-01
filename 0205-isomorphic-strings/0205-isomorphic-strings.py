class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashSt = {}

        for i in range(len(s)):
            if s[i] not in hashSt.keys():
                if t[i] in hashSt.values():
                    return False
                else:
                    hashSt[s[i]] = t[i]
            elif hashSt[s[i]] != t[i]:
                return False

        return True
        