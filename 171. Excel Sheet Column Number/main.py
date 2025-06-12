class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if len(columnTitle) == 1: return ord(columnTitle)-64
        output = ord(columnTitle[-1]) -64

        for x in range(1, len(columnTitle)):
            output += (26**x * (ord(columnTitle[-(x+1)])-64))
        return output