class Solution:
    def maxDifference(self, s: str) -> int:
        temp = {}

        for x in s:
            temp[x] = temp.get(x, 0) + 1
        
        odd = 0
        even = 100

        for x in temp:
            if temp[x] %2 == 0 and temp[x] < even:
                even = temp[x]
            elif temp[x] % 2 != 0 and temp[x] > odd:
                odd = temp[x]
        
        return odd - even
