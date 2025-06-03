class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            'I':1,
            'V':5,
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000}
        
        output = 0

        for x in range(len(s)-1):
            if roman[s[x+1]]>roman[s[x]]:
                output-=roman[s[x]]
            else:
                output+=roman[s[x]]
        return output+roman[s[-1]]
            