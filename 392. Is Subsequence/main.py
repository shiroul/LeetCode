class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return True if len(s) == 0 else self.function(s,t)

    def function(self, s, t):
        index = 0
        for x in t:
            if x == s[index]:
                index+=1
                if index == len(s):
                    return True
        return False