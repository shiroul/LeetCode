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

        output = pastValue = 0


        for x in reversed(s):
            currentValue = roman[x]
            if currentValue < pastValue:
                output -= currentValue
            else:
                output += currentValue
            pastValue = currentValue
        return output