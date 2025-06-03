class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        temp = {}

        if len(s) != len(pattern): return False
        for x in range(len(pattern)):
            
            if pattern[x] not in temp:
                if s[x] in temp.values():
                    return False
                temp[pattern[x]] = s[x]
            if temp[pattern[x]] != s[x]:
                return False
        return True