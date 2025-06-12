class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(31):
            temp = 2 ** x
            if temp == n:
                return True
            if temp > n:
                break
        return False