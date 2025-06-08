class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chrCount = {}

        for x in range(len(s)):
            if s[x] not in chrCount:
                if t[x] in chrCount.values():
                    return False
                chrCount[s[x]] = t[x]
            elif chrCount[s[x]] != t[x]: return False
        
        return True
