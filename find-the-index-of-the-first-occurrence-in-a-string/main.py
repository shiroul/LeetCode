class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for x in range(len(haystack) - len(needle)+1):
            if haystack[x:x+len(needle)] == needle:
                return x
        return -1
            