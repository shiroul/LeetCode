class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)

        while len(s) != 1:
            temp = 0
            for x in s:
                temp+=int(x)
            s = str(temp)
        return int(s)