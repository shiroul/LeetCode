class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = {}

        if len(s) != len(t):return False

        for x in range(len(s)):
            temp[s[x]] = temp.get(s[x], 0) + 1
            temp[t[x]] = temp.get(t[x], 0) - 1
        
        for x in temp:
            if temp[x] != 0 : return False
        return True