class Solution:
    def isValid(self, s: str) -> bool:
        openingBracket = {'(': ')', '[': ']', '{': '}'}
        openingStack = []

        for x in s:
            if x in openingBracket:
                openingStack.append(openingBracket[x])
            elif len(openingStack) == 0:return False
            elif openingStack[-1] == x:openingStack.pop()
            else:return False
        return True if len(openingStack) == 0 else False
    