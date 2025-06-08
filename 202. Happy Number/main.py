class Solution:
    def isHappy(self, n: int) -> bool:
        memo = []
        return self.happy(n, memo)

    def happy(self, n, memo):
        if n in memo: return False
        if n == 1 :return True

        memo.append(n)
        sumN = sum([int(x)**2 for x in str(n)])
        return self.happy(sumN, memo)