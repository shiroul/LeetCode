class Solution:
    def maxScore(self, s: str) -> int:
        countOne = 0
        countZero = 0

        for x in s:
            if x == '0':
                countZero +=1
                continue
            countOne+=1
        
        temp = 0
        maximum = -1

        for x in range(len(s)-1):
            if s[x] == '0':
                temp+=1
            else:
                countOne-=1
            if temp + countOne > maximum:
                maximum = temp+countOne
        
        return maximum