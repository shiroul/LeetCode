class Solution:
    def isValid(self, s: str) -> bool:
        inputDict = {')': '(', ']': '[', '}': '{'}
        temp = []

        for x in s:
            if x in inputDict:
                if not temp:
                    return False
                if inputDict[x] == temp[-1]:
                    temp.pop()
                    continue
                break
            temp.append(x)
        
        return True if len(temp) == 0 else False
    